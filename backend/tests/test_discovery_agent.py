import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app.agents.discovery_agent import DiscoveryAgent


class DiscoveryAgentTests(unittest.TestCase):
    def test_broad_profile_does_not_cut_off_available_scholarships(self):
        agent = DiscoveryAgent()
        profile = {
            "course": "",
            "branch": "",
            "state": "",
            "category": "",
            "gender": "",
        }

        results = agent.run(profile)

        self.assertGreaterEqual(len(results), 22)


if __name__ == "__main__":
    unittest.main()
