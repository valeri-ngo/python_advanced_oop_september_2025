from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    VALID_TYPES = {
        'RenaissanceArtifact': RenaissanceArtifact,
        'ContemporaryArtifact': ContemporaryArtifact,
    }

    VALID_COLLECTORS = {
        'Museum': Museum,
        'PrivateCollector': PrivateCollector
    }

    def __init__(self):
        self.artifacts = []
        self.collectors = []


    def register_artifact(self,
                          artifact_type: str,
                          artifact_name: str,
                          artifact_price: float,
                          artifact_space: int
                          ):
        if artifact_type not in self.VALID_TYPES:
            raise ValueError('Unknown artifact type!')

        if self._find_obj_by_name(artifact_name, self.artifacts) is not None:
            raise ValueError(f"{artifact_name} has been already registered!")

        new_artifact = self.VALID_TYPES[artifact_type](
            artifact_name,
            artifact_price,
            artifact_space
        )

        self.artifacts.append(new_artifact)
        return f'{artifact_name} is successfully added to the auction as {artifact_type}.'


    def register_collector(self,
                           collector_type: str,
                           collector_name: str
                           ):

        cls = self.VALID_COLLECTORS.get(collector_type)

        if cls is None:
            raise ValueError("Unknown collector type!")

        if self._find_obj_by_name(collector_name, self.collectors) is not None:
            raise ValueError(f"{collector_name} has been already registered!")

        new_collector = cls(collector_name)
        self.collectors.append(new_collector)
        return f"{collector_name} is successfully registered as a {collector_type}."


    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = self._find_obj_by_name(collector_name, self.collectors)
        if collector is None:
            raise ValueError(f'Collector {collector_name} is not registered to the auction!')

        artifact = self._find_obj_by_name(artifact_name, self.artifacts)
        if artifact is None:
            raise ValueError(f'Artifact {artifact_name} is not registered to the auction!')

        artifact_price = getattr(artifact, 'price', None)
        artifact_space = getattr(artifact, 'space_required', getattr(artifact, 'space', None))

        if not collector.can_purchase(artifact_price, artifact_space):
            return 'Purchase is impossible.'

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact_price
        collector.available_space -= artifact_space

        return f'{collector_name} purchased {artifact_name} for a price of {artifact_price:.2f}.'


    def remove_artifact(self, artifact_name: str):
        artifact = self._find_obj_by_name(artifact_name, self.artifacts)
        if artifact is None:
            return 'No such artifact.'

        info = artifact.artifact_information()
        self.artifacts.remove(artifact)
        return f'Removed {info}'


    def fundraising_campaigns(self, max_money: float):
        counter = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                counter += 1
        return f'{counter} collector/s increased their available money.'


    def get_auction_report(self):
        sorted_by_purchase = sorted(self.collectors, key= lambda x : (-len(x.purchased_artifacts), x.name))
        sold_count = sum(len(a.purchased_artifacts) for a in self.collectors)

        report = ['**Auction statistics**']
        report.append(f'Total number of sold artifacts: {sold_count}')
        report.append(f'Available artifacts for sale: {len(self.artifacts)}')
        report.append('***')
        report.extend(str(c) for c in sorted_by_purchase)

        return '\n'.join(report)


    @staticmethod
    def _find_obj_by_name(obj_name, collection):
        return next((obj for obj in collection if obj.name == obj_name), None)


