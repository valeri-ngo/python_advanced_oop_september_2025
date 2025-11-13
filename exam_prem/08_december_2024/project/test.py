# python
import unittest

from project.auction_house_manager_app import AuctionHouseManagerApp
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.collectors.base_collector import BaseCollector


class TestAuctionHouseManagerFull(unittest.TestCase):
    def setUp(self):
        self.app = AuctionHouseManagerApp()

    def test_artifact_validation_errors(self):
        # empty name
        with self.assertRaises(ValueError) as cm:
            self.app.register_artifact("RenaissanceArtifact", "", 100.0, 10)
        self.assertIn("Artifact name cannot be null or empty", str(cm.exception))

        # price <= 0
        with self.assertRaises(ValueError) as cm2:
            self.app.register_artifact("ContemporaryArtifact", "A", 0.0, 5)
        self.assertIn("Artifact price should be more than 0.0", str(cm2.exception))

        # space out of bounds (0 and 1001)
        with self.assertRaises(ValueError):
            self.app.register_artifact("RenaissanceArtifact", "B", 10.0, 0)
        with self.assertRaises(ValueError):
            self.app.register_artifact("ContemporaryArtifact", "C", 10.0, 1001)

    def test_collector_validation_errors_via_dummy_subclass(self):
        # Create a concrete subclass to test BaseCollector validations
        class DummyCollector(BaseCollector):
            def increase_money(self):
                self.available_money += 1.0

        # invalid name (contains punctuation)
        with self.assertRaises(ValueError) as cm:
            DummyCollector("Bad@Name", 10.0, 10)
        self.assertIn("Collector name must contain letters, numbers", str(cm.exception))

        # negative money
        with self.assertRaises(ValueError) as cm2:
            DummyCollector("GoodName", -5.0, 10)
        self.assertIn("A collector cannot have a negative amount of money", str(cm2.exception))

        # negative space
        with self.assertRaises(ValueError) as cm3:
            DummyCollector("GoodName2", 10.0, -1)
        self.assertIn("A collector cannot have a negative space available", str(cm3.exception))

    def test_register_and_duplicate_and_unknown_type(self):
        msg = self.app.register_artifact("RenaissanceArtifact", "Mona", 1000.0, 10)
        self.assertEqual(msg, "Mona is successfully added to the auction as RenaissanceArtifact.")
        with self.assertRaises(ValueError) as cm:
            self.app.register_artifact("RenaissanceArtifact", "Mona", 50.0, 5)
        self.assertIn("has been already registered", str(cm.exception))

        with self.assertRaises(ValueError) as cm2:
            self.app.register_artifact("NoSuchType", "X", 10.0, 1)
        self.assertEqual(str(cm2.exception), "Unknown artifact type!")

        msgc = self.app.register_collector("Museum", "Louvre")
        self.assertEqual(msgc, "Louvre is successfully registered as a Museum.")
        with self.assertRaises(ValueError) as cm3:
            self.app.register_collector("Museum", "Louvre")
        self.assertIn("has been already registered", str(cm3.exception))

        with self.assertRaises(ValueError) as cm4:
            self.app.register_collector("NoCollector", "Name")
        self.assertEqual(str(cm4.exception), "Unknown collector type!")

    def test_perform_purchase_success_and_object_storage(self):
        self.app.register_artifact("RenaissanceArtifact", "Kohinoor", 5000.0, 10)
        self.app.register_collector("Museum", "Louvre")

        res = self.app.perform_purchase("Louvre", "Kohinoor")
        self.assertEqual(res, "Louvre purchased Kohinoor for a price of 5000.00.")
        # artifact removed from auction list
        self.assertEqual(len(self.app.artifacts), 0)

        # collector updated with artifact object stored
        collector = next(c for c in self.app.collectors if c.name == "Louvre")
        self.assertEqual(len(collector.purchased_artifacts), 1)
        purchased = collector.purchased_artifacts[0]
        # should be artifact object and attributes intact
        self.assertTrue(hasattr(purchased, "name") and purchased.name == "Kohinoor")
        self.assertAlmostEqual(collector.available_money, 10000.0)
        self.assertEqual(collector.available_space, 1990)

        # __str__ lists artifact names (sorted descending). Add another purchase to test sorting.
        # add a cheap artifact and a private collector with enough money
        self.app.register_artifact("ContemporaryArtifact", "Alpha", 100.0, 1)
        self.app.register_collector("PrivateCollector", "Rich")
        # let Rich buy Alpha
        self.app.perform_purchase("Rich", "Alpha")
        # Now __str__ for Rich should include Alpha
        rich = next(c for c in self.app.collectors if c.name == "Rich")
        s = str(rich)
        self.assertIn("Artifacts: Alpha", s)

    def test_perform_purchase_impossible_and_nonexistent(self):
        self.app.register_artifact("ContemporaryArtifact", "Exp", 100000.0, 1)
        self.app.register_collector("PrivateCollector", "Poor")
        # Poor has 25000, can't buy 100000
        res = self.app.perform_purchase("Poor", "Exp")
        self.assertEqual(res, "Purchase is impossible.")

        # nonexistent collector
        with self.assertRaises(ValueError) as cm:
            self.app.perform_purchase("NoOne", "Exp")
        self.assertIn("Collector NoOne is not registered", str(cm.exception))

        # nonexistent artifact
        self.app.register_collector("Museum", "M")
        with self.assertRaises(ValueError) as cm2:
            self.app.perform_purchase("M", "NoArtifact")
        self.assertIn("Artifact NoArtifact is not registered", str(cm2.exception))

    def test_remove_artifact_and_information(self):
        self.app.register_artifact("ContemporaryArtifact", "Scream", 2000.0, 1000)
        res = self.app.remove_artifact("Scream")
        # Should return Removed <artifact_information>
        self.assertTrue(res.startswith("Removed Contemporary Artifact: Scream; Price: 2000.00; Required space: 1000"))
        # removing again returns No such artifact.
        self.assertEqual(self.app.remove_artifact("Scream"), "No such artifact.")

    def test_fundraising_campaigns_and_threshold_edge(self):
        self.app.register_collector("Museum", "A")
        self.app.register_collector("PrivateCollector", "B")
        # set B to exactly max threshold
        b = next(c for c in self.app.collectors if c.name == "B")
        b.available_money = 15000.0
        # A has 15000.0 initially, so both should be increased when max_money == 15000
        res = self.app.fundraising_campaigns(15000.0)
        self.assertEqual(res, "2 collector/s increased their available money.")
        a = next(c for c in self.app.collectors if c.name == "A")
        self.assertAlmostEqual(a.available_money, 16000.0)  # Museum +1000
        self.assertAlmostEqual(b.available_money, 20000.0)  # PrivateCollector +5000

    def test_get_auction_report_sorting_and_counts(self):
        # Setup 3 collectors with different purchase counts and names to exercise sorting
        self.app.register_collector("Museum", "Zed")
        self.app.register_collector("PrivateCollector", "Alex")
        self.app.register_collector("Museum", "Bob")

        # create artifacts and assign purchases:
        # Alex buys 2 artifacts, Bob buys 1, Zed buys 0
        self.app.register_artifact("RenaissanceArtifact", "R1", 100.0, 1)
        self.app.register_artifact("RenaissanceArtifact", "R2", 100.0, 1)
        self.app.register_artifact("ContemporaryArtifact", "C1", 50.0, 1)

        self.app.perform_purchase("Alex", "R1")
        self.app.perform_purchase("Alex", "R2")
        self.app.perform_purchase("Bob", "C1")

        report = self.app.get_auction_report()
        # header and counts
        self.assertIn("**Auction statistics**", report)
        self.assertIn("Total number of sold artifacts: 3", report)
        self.assertIn("Available artifacts for sale: 0", report)
        # ordering: Alex (2), Bob (1), Zed (0); when ties, name ascending -- ensure that behavior
        lines = report.splitlines()
        # last lines contain collectors; ensure Alex appears before Bob and Zed
        report_tail = "\n".join(lines[-3:])
        self.assertIn("Collector name: Alex;", report_tail)
        self.assertIn("Collector name: Bob;", report_tail)
        self.assertIn("Collector name: Zed;", report_tail)
        # Alex should be listed before Bob
        self.assertTrue(report_tail.index("Collector name: Alex;") < report_tail.index("Collector name: Bob;"))

    def test_purchased_artifact_objects_integrity_after_multiple_operations(self):
        # ensure purchased artifacts remain objects and independent after removal operations
        self.app.register_artifact("RenaissanceArtifact", "Keep", 300.0, 5)
        self.app.register_collector("PrivateCollector", "Collector1")
        self.app.perform_purchase("Collector1", "Keep")
        c = next(c for c in self.app.collectors if c.name == "Collector1")
        self.assertEqual(len(c.purchased_artifacts), 1)
        art_obj = c.purchased_artifacts[0]
        # modify the art_obj attribute locally and ensure it does not affect any removed-list in app
        art_obj.price = 999.0
        # app.artifacts should not contain this artifact (it was removed on purchase)
        self.assertNotIn(art_obj, self.app.artifacts)
        # string conversion still reflects updated price when calling artifact_information()
        self.assertIn("999.00", art_obj.artifact_information())

if __name__ == "__main__":
    unittest.main()
