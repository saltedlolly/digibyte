#!/usr/bin/env python3
# Copyright (c) 2021 The DigiByte Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from test_framework.test_framework import DigiByteTestFramework
from test_framework.util import assert_equal

class GetBlockRewardTest(DigiByteTestFramework):
    def set_test_params(self):
        self.num_nodes = 1
        self.setup_clean_chain = True

    def run_test(self):
        node = self.nodes[0]

        # Mine some blocks
        self.generatetoaddress(101, node.get_deterministic_priv_key().address)

        # Test getblockreward RPC
        block_reward = node.getblockreward()
        self.log.info("Current block reward: {}".format(block_reward["blockreward"]))
        assert_equal(block_reward["blockreward"], <expected_block_reward>)

if __name__ == '__main__':
    GetBlockRewardTest().main()
