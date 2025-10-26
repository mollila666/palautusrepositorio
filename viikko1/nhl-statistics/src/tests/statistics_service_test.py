import unittest
from statistics_service import StatisticsService
from player import Player

# StubReader ei käytä verkkoa
class StubReader:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(StubReader())

    def test_search_finds_player(self):
        player = self.stats.search("Lemieux")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Lemieux")

    def test_search_returns_none_if_not_found(self):
        player = self.stats.search("Selänne")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        team_players = self.stats.team("EDM")
        names = [p.name for p in team_players]
        self.assertListEqual(sorted(names), sorted(["Semenko", "Kurri", "Gretzky"]))

    def test_top_returns_right_amount(self):
        top_players = self.stats.top(2)
        # top(2) palauttaa 3 ensimmäistä: 0, 1 ja 2
        self.assertEqual(len(top_players), 3)

    def test_top_returns_correct_order(self):
        top_players = self.stats.top(0)
        # top(0) palauttaa yhden: parhaimman pistemiehen
        self.assertEqual(top_players[0].name, "Gretzky")