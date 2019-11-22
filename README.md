
## TM
* <span id = "strategy">tri_abci_info</span>

    * @apiName：http://192.168.1.141:46657/tri_abci_info

    * @api：{get}

    * @apiParam：

    * @apiSuccessExample Success-Response:：
           
             {
                  "jsonrpc": "2.0",
                   "id": "",
                   "result": {
                   "response": {
                   "data": "{\"size\":67824}",
                   "version": "0.16.0",
                   "app_version": "1",
                   "last_block_height": "8874",
                    "last_block_app_hash": "N45TS4L7kL8I28UcfnL3kCvw0LE="
                      }
                    }
              }
              
---
* <span id = "strategy">tri_api_list</span>

    * @apiName：http://192.168.1.141:46657/tri_api_list

    * @api：{get}

    * @apiParam：

    * @apiSuccessExample Success-Response:：
           
            {
              "jsonrpc": "2.0",
              "id": "",
              "result": {
                "node_info": {
                  "protocol_version": {
                    "p2p": "7",
                    "block": "10",
                    "app": "1"
                  },
                  "id": "03b6e68c73806879253a3d5e073474a96925176e",
                  "listen_addr": "tcp://0.0.0.0:46656",
                  "network": "test-chain-rx2wEB",
                  "version": "0.31.8",
                  "channels": "4020212223262425303800",
                  "moniker": "ubt18-trias-dag-141",
                  "other": {
                    "tx_index": "on",
                    "rpc_address": "tcp://0.0.0.0:46657"
                  }
                },
                "sync_info": {
                  "latest_block_hash": "D86B775CD79B95B35D522D47B02B00FFB768C8C399083FAC2DCB859650B6C545",
                  "latest_app_hash": "378E534B82FB90BF08DBC51C7E72F7902BF0D0B1",
                  "latest_block_height": "8874",
                  "latest_block_time": "2019-11-11T02:13:56.879610615Z",
                  "catching_up": false
                },
                "validator_info": {
                  "address": "881F5463E5CB4276FF71A229B53072CC0213DF2B",
                  "pub_key": {
                    "type": "tendermint/PubKeyEd25519",
                    "value": "R00Mp/3CaLbOvMiCHZRxLVSha+o+RAMGynMz81BF0Uo="
                  },
                  "voting_power": "1007"
                }
              }
            }

              
---
* <span id = "strategy">tri_block_validators</span>

    * @apiName：http://192.168.1.141:46657/tri_block_validators

    * @api：{get}

    * @apiParam：

    * @apiSuccessExample Success-Response:：
    
             {
              "jsonrpc": "2.0",
              "id": "",
              "result": {
                "block_height": "8875",
                "validators": [
                  {
                    "address": "0859B4E707843D455E5D2BC92F52A368BBAB1B76",
                    "pub_key": {
                      "type": "tendermint/PubKeyEd25519",
                      "value": "hEuywjYFkOVxwqi2pPX+vCxEyaF+IBDKboFnHCJZqL0="
                    },
                    "voting_power": "1002",
                    "proposer_priority": "1801"
                  },
                  {
                    "address": "0A2E3E7599E28E5A60FF3FAB9FA2767F24A451DE",
                    "pub_key": {
                      "type": "tendermint/PubKeyEd25519",
                      "value": "DeLSPpZgD5QirdtinbKuipwhbvmoKCieGzj19A9mGYs="
                    },
                    "voting_power": "1005",
                    "proposer_priority": "-3598"
                  },
                  {
                    "address": "881F5463E5CB4276FF71A229B53072CC0213DF2B",
                    "pub_key": {
                      "type": "tendermint/PubKeyEd25519",
                      "value": "R00Mp/3CaLbOvMiCHZRxLVSha+o+RAMGynMz81BF0Uo="
                    },
                    "voting_power": "1007",
                    "proposer_priority": "-1634"
                  },
                  {
                    "address": "A8E396910669DC753D17BFC40FE600731F5C36F5",
                    "pub_key": {
                      "type": "tendermint/PubKeyEd25519",
                      "value": "GY9X2m4N5jigj4gqdh6MgvT4JapfSdo5+UHCL+173dA="
                    },
                    "voting_power": "1003",
                    "proposer_priority": "2344"
                  },
                  {
                    "address": "C788EB685AD66C93CD78A60C9E8DC938B32DF168",
                    "pub_key": {
                      "type": "tendermint/PubKeyEd25519",
                      "value": "nFQX4cscivXuP7i9SJi2ogeN9sJtRuF8Zn185jHM7wY="
                    },
                    "voting_power": "1001",
                    "proposer_priority": "1258"
                  },
                  {
                    "address": "EDA2EC8A111C015D38D10D09F95F417C46DBF6E7",
                    "pub_key": {
                      "type": "tendermint/PubKeyEd25519",
                      "value": "PEU38XIQaZo0JkcUVH65IhxmCVbYi+byMvXcqvTs63Y="
                    },
                    "voting_power": "1006",
                    "proposer_priority": "-3055"
                  },
                  {
                    "address": "F061FEC70049C4CCCB45A2B15E59BFDD9AFBE9C8",
                    "pub_key": {
                      "type": "tendermint/PubKeyEd25519",
                      "value": "9NRZoxuwnClhmBZ/H1wE6/1+LMpUuZiHd5+SviX3W9c="
                    },
                    "voting_power": "1004",
                    "proposer_priority": "2887"
                  }
                ]
              }
            }

---
* <span id = "strategy">tri_block_info</span>

    * @apiName：http://192.168.1.141:46657/tri_block_info

    * @api：{get}

    * @apiParam：

    * @apiSuccessExample Success-Response:：
            
            {
              "jsonrpc": "2.0",
              "id": "",
              "result": {
                "block_meta": {
                  "block_id": {
                    "hash": "FCD02B8AF701DB13435696415B0607AB67F3477EE0D04CF2F5CB9A3D1C818ED1",
                    "parts": {
                      "total": "1",
                      "hash": "EF9263BDFD1E51F7A9A94D8D4FADE216B37CCB6E03483DA9B67096203F193724"
                    }
                  },
                  "header": {
                    "version": {
                      "block": "10",
                      "app": "1"
                    },
                    "chain_id": "test-chain-rx2wEB",
                    "height": "8876",
                    "time": "2019-11-12T01:51:22.116283024Z",
                    "num_txs": "0",
                    "total_txs": "67819",
                    "last_block_id": {
                      "hash": "FF152C5A7F5118C8D734CE226B7FECF4B3A33B781B413A6165A45C35FF80AC51",
                      "parts": {
                        "total": "1",
                        "hash": "CE1369D274D32288D926E13F3F2742876EB2A2DEA8EB8D346307A8A55CAA13E0"
                      }
                    },
                    "last_commit_hash": "B1CFDCE15C5CADD10E292706601C3ACEB0C67464DD0E5611CAC81C98421AFE59",
                    "data_hash": "",
                    "validators_hash": "21B4A15832BD5AFA4558FC9ABF9491A5625191AE179E6A9CE9CBCCE6EDCD9C03",
                    "next_validators_hash": "1833360CD55F80843A8D024CD4F78272E2A2DCB1AA2E3ABA93D139D4CA22C940",
                    "consensus_hash": "048091BC7DDC283F77BFBF91D73C44DA58C3DF8A9CBC867405D8B7F3DAADA22F",
                    "app_hash": "0DBA8296740C3AD831F7CE9961007822AD539A6D",
                    "last_results_hash": "6E340B9CFFB37A989CA544E6BB780A2C78901D3FB33738768511A30617AFA01D",
                    "evidence_hash": "",
                    "proposer_address": "F061FEC70049C4CCCB45A2B15E59BFDD9AFBE9C8"
                  }
                },
                "block": {
                  "header": {
                    "version": {
                      "block": "10",
                      "app": "1"
                    },
                    "chain_id": "test-chain-rx2wEB",
                    "height": "8876",
                    "time": "2019-11-12T01:51:22.116283024Z",
                    "num_txs": "0",
                    "total_txs": "67819",
                    "last_block_id": {
                      "hash": "FF152C5A7F5118C8D734CE226B7FECF4B3A33B781B413A6165A45C35FF80AC51",
                      "parts": {
                        "total": "1",
                        "hash": "CE1369D274D32288D926E13F3F2742876EB2A2DEA8EB8D346307A8A55CAA13E0"
                      }
                    },
                    "last_commit_hash": "B1CFDCE15C5CADD10E292706601C3ACEB0C67464DD0E5611CAC81C98421AFE59",
                    "data_hash": "",
                    "validators_hash": "21B4A15832BD5AFA4558FC9ABF9491A5625191AE179E6A9CE9CBCCE6EDCD9C03",
                    "next_validators_hash": "1833360CD55F80843A8D024CD4F78272E2A2DCB1AA2E3ABA93D139D4CA22C940",
                    "consensus_hash": "048091BC7DDC283F77BFBF91D73C44DA58C3DF8A9CBC867405D8B7F3DAADA22F",
                    "app_hash": "0DBA8296740C3AD831F7CE9961007822AD539A6D",
                    "last_results_hash": "6E340B9CFFB37A989CA544E6BB780A2C78901D3FB33738768511A30617AFA01D",
                    "evidence_hash": "",
                    "proposer_address": "F061FEC70049C4CCCB45A2B15E59BFDD9AFBE9C8"
                  },
                  "data": {
                    "txs": null
                  },
                  "evidence": {
                    "evidence": null
                  },
                  "last_commit": {
                    "block_id": {
                      "hash": "FF152C5A7F5118C8D734CE226B7FECF4B3A33B781B413A6165A45C35FF80AC51",
                      "parts": {
                        "total": "1",
                        "hash": "CE1369D274D32288D926E13F3F2742876EB2A2DEA8EB8D346307A8A55CAA13E0"
                      }
                    },
                    "precommits": [
                      {
                        "type": 2,
                        "height": "8875",
                        "round": "0",
                        "block_id": {
                          "hash": "FF152C5A7F5118C8D734CE226B7FECF4B3A33B781B413A6165A45C35FF80AC51",
                          "parts": {
                            "total": "1",
                            "hash": "CE1369D274D32288D926E13F3F2742876EB2A2DEA8EB8D346307A8A55CAA13E0"
                          }
                        },
                        "timestamp": "2019-11-12T01:51:22.116283024Z",
                        "validator_address": "0859B4E707843D455E5D2BC92F52A368BBAB1B76",
                        "validator_index": "0",
                        "signature": "yEuHmILOgz+5yZ/CMFb3A8EggVFpeZ5WZwzsZ5LS/0lI7LmKupmgz+AdLIpaoXtL/Ck00GnIa9QyiPF85PVRAw=="
                      },
                      {
                        "type": 2,
                        "height": "8875",
                        "round": "0",
                        "block_id": {
                          "hash": "FF152C5A7F5118C8D734CE226B7FECF4B3A33B781B413A6165A45C35FF80AC51",
                          "parts": {
                            "total": "1",
                            "hash": "CE1369D274D32288D926E13F3F2742876EB2A2DEA8EB8D346307A8A55CAA13E0"
                          }
                        },
                        "timestamp": "2019-11-12T01:51:22.144723227Z",
                        "validator_address": "0A2E3E7599E28E5A60FF3FAB9FA2767F24A451DE",
                        "validator_index": "1",
                        "signature": "Ld/ClG+yHUng64PUKsLKjROu3WYV30Lt4wLo22jNGmfAJc38zTwr9fLb2cy+O/rFXvKOSmCiJSmiuNIwqy/1Dg=="
                      },
                      {
                        "type": 2,
                        "height": "8875",
                        "round": "0",
                        "block_id": {
                          "hash": "FF152C5A7F5118C8D734CE226B7FECF4B3A33B781B413A6165A45C35FF80AC51",
                          "parts": {
                            "total": "1",
                            "hash": "CE1369D274D32288D926E13F3F2742876EB2A2DEA8EB8D346307A8A55CAA13E0"
                          }
                        },
                        "timestamp": "2019-11-12T01:51:22.02489974Z",
                        "validator_address": "881F5463E5CB4276FF71A229B53072CC0213DF2B",
                        "validator_index": "2",
                        "signature": "Hc7mCY/nUGFlbkScsOyiaOxBrjKifk7SdaVBnrV/5m1jFNU6ZnkrpNhFuWC/Gd8vbJLmq9GoqyD/EQ+2In0KDQ=="
                      },
                      {
                        "type": 2,
                        "height": "8875",
                        "round": "0",
                        "block_id": {
                          "hash": "FF152C5A7F5118C8D734CE226B7FECF4B3A33B781B413A6165A45C35FF80AC51",
                          "parts": {
                            "total": "1",
                            "hash": "CE1369D274D32288D926E13F3F2742876EB2A2DEA8EB8D346307A8A55CAA13E0"
                          }
                        },
                        "timestamp": "2019-11-12T01:51:22.104417493Z",
                        "validator_address": "A8E396910669DC753D17BFC40FE600731F5C36F5",
                        "validator_index": "3",
                        "signature": "PAxqA02PbMQSGcXApkaQ13VlPq4PZOmeHY5lUl7RWNi5bIMYiKero5WIweYarEYNHFGBMfKK+dGyh3uweuKkCw=="
                      },
                      {
                        "type": 2,
                        "height": "8875",
                        "round": "0",
                        "block_id": {
                          "hash": "FF152C5A7F5118C8D734CE226B7FECF4B3A33B781B413A6165A45C35FF80AC51",
                          "parts": {
                            "total": "1",
                            "hash": "CE1369D274D32288D926E13F3F2742876EB2A2DEA8EB8D346307A8A55CAA13E0"
                          }
                        },
                        "timestamp": "2019-11-12T01:51:22.072708368Z",
                        "validator_address": "C788EB685AD66C93CD78A60C9E8DC938B32DF168",
                        "validator_index": "4",
                        "signature": "2yBoV3juPDCGEoJ1RMyecUIUN/e+FM8E5qAw3Rls0UsgG/EqksTRDWCjHdGNgq7x/pKXyk1bD7f8x82W4iHvAg=="
                      },
                      {
                        "type": 2,
                        "height": "8875",
                        "round": "0",
                        "block_id": {
                          "hash": "FF152C5A7F5118C8D734CE226B7FECF4B3A33B781B413A6165A45C35FF80AC51",
                          "parts": {
                            "total": "1",
                            "hash": "CE1369D274D32288D926E13F3F2742876EB2A2DEA8EB8D346307A8A55CAA13E0"
                          }
                        },
                        "timestamp": "2019-11-12T01:51:22.124055006Z",
                        "validator_address": "EDA2EC8A111C015D38D10D09F95F417C46DBF6E7",
                        "validator_index": "5",
                        "signature": "ad6Ivcf5JmqZxZKF+/Bf+To8T1Q9g6x0lBxs6UMsysTDEYwK3RiLGo9wZykVtUL46lzdG7z5C8l0blFIk/LHBA=="
                      },
                      {
                        "type": 2,
                        "height": "8875",
                        "round": "0",
                        "block_id": {
                          "hash": "FF152C5A7F5118C8D734CE226B7FECF4B3A33B781B413A6165A45C35FF80AC51",
                          "parts": {
                            "total": "1",
                            "hash": "CE1369D274D32288D926E13F3F2742876EB2A2DEA8EB8D346307A8A55CAA13E0"
                          }
                        },
                        "timestamp": "2019-11-12T01:51:22.195993516Z",
                        "validator_address": "F061FEC70049C4CCCB45A2B15E59BFDD9AFBE9C8",
                        "validator_index": "6",
                        "signature": "9LAsnvIRNvHC+wTEgFg3PrmqBmo7UF08D9A773IsLtRIYha9+6RBvsu8RuwOFVYJt1dxDnciLn4Wjoh0jlKTAg=="
                      }
                    ]
                  }
                }
              }
            }

---
* <span id = "strategy">tri_blockchain_interval</span>

    * @apiName：http://192.168.1.141:46657/tri_blockchain_interval

    * @api：{get}

    * @apiParam：minHeight
    
    * @apiParam：maxHeight
    
    * @apiSuccessExample Success-Response:：
    
             {
              "jsonrpc": "2.0",
              "id": "",
              "result": {
                "last_height": "8876",
                "block_metas": [
                  {
                    "block_id": {
                      "hash": "FCD02B8AF701DB13435696415B0607AB67F3477EE0D04CF2F5CB9A3D1C818ED1",
                      "parts": {
                        "total": "1",
                        "hash": "EF9263BDFD1E51F7A9A94D8D4FADE216B37CCB6E03483DA9B67096203F193724"
                      }
                    },
                    "header": {
                      "version": {
                        "block": "10",
                        "app": "1"
                      },
                      "chain_id": "test-chain-rx2wEB",
                      "height": "8876",
                      "time": "2019-11-12T01:51:22.116283024Z",
                      "num_txs": "0",
                      "total_txs": "67819",
                      "last_block_id": {
                        "hash": "FF152C5A7F5118C8D734CE226B7FECF4B3A33B781B413A6165A45C35FF80AC51",
                        "parts": {
                          "total": "1",
                          "hash": "CE1369D274D32288D926E13F3F2742876EB2A2DEA8EB8D346307A8A55CAA13E0"
                        }
                      },
                      "last_commit_hash": "B1CFDCE15C5CADD10E292706601C3ACEB0C67464DD0E5611CAC81C98421AFE59",
                      "data_hash": "",
                      "validators_hash": "21B4A15832BD5AFA4558FC9ABF9491A5625191AE179E6A9CE9CBCCE6EDCD9C03",
                      "next_validators_hash": "1833360CD55F80843A8D024CD4F78272E2A2DCB1AA2E3ABA93D139D4CA22C940",
                      "consensus_hash": "048091BC7DDC283F77BFBF91D73C44DA58C3DF8A9CBC867405D8B7F3DAADA22F",
                      "app_hash": "0DBA8296740C3AD831F7CE9961007822AD539A6D",
                      "last_results_hash": "6E340B9CFFB37A989CA544E6BB780A2C78901D3FB33738768511A30617AFA01D",
                      "evidence_hash": "",
                      "proposer_address": "F061FEC70049C4CCCB45A2B15E59BFDD9AFBE9C8"
                    }
                  }
              }
            }
            
---
* <span id = "strategy">tri_bc_tx_async</span>

    * @apiName：http://192.168.1.141:46657/tri_bc_tx_async

    * @api：{get}

    * @apiParam：tx
    
    * @apiSuccessExample Success-Response:：
                
            {
              "jsonrpc": "2.0",
              "id": "",
              "result": {
                "code": 0,
                "data": "",
                "log": "",
                "hash": "C8F17AA3210DE569D147D3350D356F018747C16794A5996E5CC6A71A8588D423"
              }
            }
---
* <span id = "strategy">tri_bc_tx_commit</span>

    * @apiName：http://192.168.1.141:46657/tri_bc_tx_commit

    * @api：{get}

    * @apiParam：tx
    
    * @apiSuccessExample Success-Response:：
    
                {
              "jsonrpc": "2.0",
              "id": "",
              "result": {
                "check_tx": {
                  "gasWanted": "1"
                },
                "deliver_tx": {
                  "tags": [
                    {
                      "key": "YXBwLmNyZWF0b3I=",
                      "value": "VHJpYXMgTmV0b3dva28="
                    },
                    {
                      "key": "YXBwLmtleQ==",
                      "value": "WzE1NzM1MjcwMDFdYXNkYXNkYXNk"
                    }
                  ]
                },
                "hash": "84B430D7072DF2E16C68D2C98FEFF78E45922E3C6E2F99907286A1F3DC350668",
                "height": "8881"
              }
            }
     
---
* <span id = "strategy">tri_abci_query</span>

    * @apiName：http://192.168.1.141:46657/tri_abci_query

    * @api：{get}

    * @apiParam：path
    
    * @apiParam  data
    
    * @apiParam  prove
    
    * @apiSuccessExample Success-Response:：
    
 ---
 * <span id = "strategy">tri_block_commit</span>

    * @apiName：http://192.168.1.141:46657/tri_block_commit

    * @api：{get}

    * @apiParam:
    
    * @apiSuccessExample Success-Response:：
    
                {
              "jsonrpc": "2.0",
              "id": "",
              "result": {
                "signed_header": {
                  "header": {
                    "version": {
                      "block": "10",
                      "app": "1"
                    },
                    "chain_id": "test-chain-rx2wEB",
                    "height": "8884",
                    "time": "2019-11-12T03:10:30.38881153Z",
                    "num_txs": "0",
                    "total_txs": "67823",
                    "last_block_id": {
                      "hash": "CDDD7FE7866A681BDE908D8FB7F195A0FAD33442D1461055506CA37BE2767982",
                      "parts": {
                        "total": "1",
                        "hash": "FDE753C026A624FE6CD89B54D2071EDC2329EBAE563FC13CF2B3BF58B56743CA"
                      }
                    },
                    "last_commit_hash": "4F276617C297B56057B44EFFC76871290AFB04C77F9D570F27AD3303ED360E7D",
                    "data_hash": "",
                    "validators_hash": "1833360CD55F80843A8D024CD4F78272E2A2DCB1AA2E3ABA93D139D4CA22C940",
                    "next_validators_hash": "1833360CD55F80843A8D024CD4F78272E2A2DCB1AA2E3ABA93D139D4CA22C940",
                    "consensus_hash": "048091BC7DDC283F77BFBF91D73C44DA58C3DF8A9CBC867405D8B7F3DAADA22F",
                    "app_hash": "40C9977A678421ABF2F722E65CAB39C31B77033E",
                    "last_results_hash": "6E340B9CFFB37A989CA544E6BB780A2C78901D3FB33738768511A30617AFA01D",
                    "evidence_hash": "",
                    "proposer_address": "A8E396910669DC753D17BFC40FE600731F5C36F5"
                  },
                  "commit": {
                    "block_id": {
                      "hash": "23B76BF79EA07497366AA436430F3253C89EFAA115E597496D94368A22F495F9",
                      "parts": {
                        "total": "1",
                        "hash": "E38F305577182764CDB5A5A567745D923259D921A67118748408696B6914D886"
                      }
                    },
                    "precommits": [
                      {
                        "type": 2,
                        "height": "8884",
                        "round": "0",
                        "block_id": {
                          "hash": "23B76BF79EA07497366AA436430F3253C89EFAA115E597496D94368A22F495F9",
                          "parts": {
                            "total": "1",
                            "hash": "E38F305577182764CDB5A5A567745D923259D921A67118748408696B6914D886"
                          }
                        },
                        "timestamp": "2019-11-12T03:10:31.70634381Z",
                        "validator_address": "881F5463E5CB4276FF71A229B53072CC0213DF2B",
                        "validator_index": "0",
                        "signature": "swdVvKI3uMFT9URvrFPgS6o+MpwMLYKUZGoyCw0cfq4oKUYUiTwOVkcVa4DXe1g72c2+twae3SzCs5+elk9pBg=="
                      },
                      {
                        "type": 2,
                        "height": "8884",
                        "round": "0",
                        "block_id": {
                          "hash": "23B76BF79EA07497366AA436430F3253C89EFAA115E597496D94368A22F495F9",
                          "parts": {
                            "total": "1",
                            "hash": "E38F305577182764CDB5A5A567745D923259D921A67118748408696B6914D886"
                          }
                        },
                        "timestamp": "2019-11-12T03:10:31.786985681Z",
                        "validator_address": "A8E396910669DC753D17BFC40FE600731F5C36F5",
                        "validator_index": "1",
                        "signature": "1OJjMOIO/feKlPomD2yMVIoNwcqkxENov8bm2zk8snMwlRPnAlksUPXvawVZRN1Sb30yXUiF/ZmAgPvpB4V3CA=="
                      }
                    ]
                  }
                },
                "canonical": false
              }
            }

---
 * <span id = "strategy">tri_block_tx</span>

    * @apiName：http://192.168.1.141:46657/tri_block_tx

    * @api：{get}

    * @apiParam:hash
    
    * @apiParam:prove
    
    * @apiSuccessExample Success-Response:：
    
    
---
 * <span id = "strategy">tri_broadcast_kernel</span>

    * @apiName：http://192.168.1.141:46657/tri_broadcast_kernel

    * @api：{get}

    * @apiParam:data
    
    * @apiSuccessExample Success-Response::
    
            {
              "jsonrpc": "2.0",
              "id": "",
              "result": {
                "code": "200",
                "log": "success"
              }
            }

---
 * <span id = "strategy">tri_broadcast_msg</span>

    * @apiName：http://192.168.1.141:46657/tri_broadcast_msg

    * @api：{get}

    * @apiParam:data
    
    * @apiSuccessExample Success-Response::
    
            {
              "jsonrpc": "2.0",
              "id": "",
              "result": {
                "code": "200",
                "log": "success"
              }
            }
---
 * <span id = "strategy">tri_broadcast_prove</span>

    * @apiName：http://192.168.1.141:46657/tri_broadcast_prove

    * @api：{get}

    * @apiParam:data
    
    * @apiSuccessExample Success-Response::
    
              {
              "jsonrpc": "2.0",
              "id": "",
              "result": {
                "code": "200",
                "log": "success"
              }
              
---
 * <span id = "strategy">tri_get_subscribe</span>

    * @apiName：http://192.168.1.141:46657/tri_get_subscribe

    * @api：{get}

    * @apiParam:event
    
    * @apiSuccessExample Success-Response::
    
---

 * <span id = "strategy">tri_get_unsubscribe</span>

    * @apiName：http://192.168.1.141:46657/tri_get_unsubscribe

    * @api：{get}

    * @apiParam:event
    
    * @apiSuccessExample Success-Response::
    
---
 * <span id = "strategy">tri_net_info</span>

    * @apiName：http://192.168.1.141:46657/tri_net_info

    * @api：{get}

    * @apiParam:event
    
    * @apiSuccessExample Success-Response::
    
             {
              "jsonrpc": "2.0",
              "id": "",
              "result": {
                "listening": true,
                "listeners": [
                  "Listener(@)"
                ],
                "n_peers": "7",
                "peers": [
                  {
                    "node_info": {
                      "protocol_version": {
                        "p2p": "7",
                        "block": "10",
                        "app": "1"
                      },
                      "id": "79f24251c9a3e5ec625be6f94fab1072a2f6ac06",
                      "listen_addr": "tcp://0.0.0.0:46656",
                      "network": "test-chain-rx2wEB",
                      "version": "0.31.8",
                      "channels": "4020212223262425303800",
                      "moniker": "ubt18-trias-dag-143",
                      "other": {
                        "tx_index": "on",
                        "rpc_address": "tcp://0.0.0.0:46657"
                      }
                    },
                    "is_outbound": false,
                    "connection_status": {
                      "Duration": "256412628860794",
                      "SendMonitor": {
                        "Active": true,
                        "Start": "2019-11-09T07:40:45.14Z",
                        "Duration": "256412620000000",
                        "Idle": "2700000000",
                        "Bytes": "11914642",
                        "Samples": "38806",
                        "InstRate": "5",
                        "CurRate": "9",
                        "AvgRate": "46",
                        "PeakRate": "143158",
                        "BytesRem": "0",
                        "TimeRem": "0",
                        "Progress": 0
                      },
                      "RecvMonitor": {
                        "Active": true,
                        "Start": "2019-11-09T07:40:45.14Z",
                        "Duration": "256412620000000",
                        "Idle": "2580000000",
                        "Bytes": "2260525",
                        "Samples": "37899",
                        "InstRate": "0",
                        "CurRate": "14",
                        "AvgRate": "9",
                        "PeakRate": "26700",
                        "BytesRem": "0",
                        "TimeRem": "0",
                        "Progress": 0
                      },
                      "Channels": [
                        {
                          "ID": 48,
                          "SendQueueCapacity": "1",
                          "SendQueueSize": "0",
                          "Priority": "5",
                          "RecentlySent": "0"
                        },
                        {
                          "ID": 64,
                          "SendQueueCapacity": "1000",
                          "SendQueueSize": "0",
                          "Priority": "10",
                          "RecentlySent": "0"
                        },
                         "remote_ip": "192.168.1.146"
                  }
                ]
              }
            }


---
 * <span id = "strategy">tri_dump_consensus_state</span>

    * @apiName：http://192.168.1.141:46657/tri_dump_consensus_state

    * @api：{get}

    * @apiParam:
   
    * @apiSuccessExample Success-Response::
    
               {
                 "jsonrpc": "2.0",
                 "id": "",
                 "result": {
                   "round_state": {
                     "height": "8885",
                     "round": "0",
                     "step": 2,
                     "start_time": "2019-11-12T03:10:32.906211321Z",
                     "commit_time": "2019-11-12T03:10:31.906211321Z",
                     "validators": {
                       "validators": [
                         {
                           "address": "881F5463E5CB4276FF71A229B53072CC0213DF2B",
                           "pub_key": {
                             "type": "tendermint/PubKeyEd25519",
                             "value": "R00Mp/3CaLbOvMiCHZRxLVSha+o+RAMGynMz81BF0Uo="
                           },
                           "voting_power": "1002",
                           "proposer_priority": "-981"
                         },
                         {
                           "address": "A8E396910669DC753D17BFC40FE600731F5C36F5",
                           "pub_key": {
                             "type": "tendermint/PubKeyEd25519",
                             "value": "GY9X2m4N5jigj4gqdh6MgvT4JapfSdo5+UHCL+173dA="
                           },
                           "voting_power": "1001",
                           "proposer_priority": "981"
                         }
                       ],
                       "proposer": {
                         "address": "881F5463E5CB4276FF71A229B53072CC0213DF2B",
                         "pub_key": {
                           "type": "tendermint/PubKeyEd25519",
                           "value": "R00Mp/3CaLbOvMiCHZRxLVSha+o+RAMGynMz81BF0Uo="
                         },
                         "voting_power": "1002",
                         "proposer_priority": "-981"
                       }
                     },
                     "proposal": null,
                     "proposal_block": null,
                     "proposal_block_parts": null,
                     "locked_round": "-1",
                     "locked_block": null,
                     "locked_block_parts": null,
                     "valid_round": "-1",
                     "valid_block": null,
                     "valid_block_parts": null,
                     "votes": [
                       {
                         "round": "0",
                         "prevotes": [
                           "nil-Vote",
                           "nil-Vote"
                         ],
                         "prevotes_bit_array": "BA{2:__} 0/2003 = 0.00",
                         "precommits": [
                           "nil-Vote",
                           "nil-Vote"
                         ],
                         "precommits_bit_array": "BA{2:__} 0/2003 = 0.00"
                       },
                       {
                         "round": "1",
                         "prevotes": [
                           "nil-Vote",
                           "nil-Vote"
                         ],
                         "prevotes_bit_array": "BA{2:__} 0/2003 = 0.00",
                         "precommits": [
                           "nil-Vote",
                           "nil-Vote"
                         ],
                         "precommits_bit_array": "BA{2:__} 0/2003 = 0.00"
                       }
                     ],
                     "commit_round": "-1",
                     "last_commit": {
                       "votes": [
                         "Vote{0:881F5463E5CB 8884/00/2(Precommit) 23B76BF79EA0 B30755BCA237 @ 2019-11-12T03:10:31.70634381Z}",
                         "Vote{1:A8E396910669 8884/00/2(Precommit) 23B76BF79EA0 D4E26330E20E @ 2019-11-12T03:10:31.786985681Z}"
                       ],
                       "votes_bit_array": "BA{2:xx} 2003/2003 = 1.00",
                       "peer_maj_23s": {}
                     },
                     "last_validators": {
                       "validators": [
                         {
                           "address": "881F5463E5CB4276FF71A229B53072CC0213DF2B",
                           "pub_key": {
                             "type": "tendermint/PubKeyEd25519",
                             "value": "R00Mp/3CaLbOvMiCHZRxLVSha+o+RAMGynMz81BF0Uo="
                           },
                           "voting_power": "1002",
                           "proposer_priority": "20"
                         },
                         {
                           "address": "A8E396910669DC753D17BFC40FE600731F5C36F5",
                           "pub_key": {
                             "type": "tendermint/PubKeyEd25519",
                             "value": "GY9X2m4N5jigj4gqdh6MgvT4JapfSdo5+UHCL+173dA="
                           },
                           "voting_power": "1001",
                           "proposer_priority": "-20"
                         }
                       ],
                       "proposer": {
                         "address": "A8E396910669DC753D17BFC40FE600731F5C36F5",
                         "pub_key": {
                           "type": "tendermint/PubKeyEd25519",
                           "value": "GY9X2m4N5jigj4gqdh6MgvT4JapfSdo5+UHCL+173dA="
                         },
                         "voting_power": "1001",
                         "proposer_priority": "-20"
                       }
                     },
                     "triggered_timeout_precommit": false
                   },
                   "peers": [
                     {
                       "node_address": "79f24251c9a3e5ec625be6f94fab1072a2f6ac06@192.168.1.143:57824",
                       "peer_state": {
                         "round_state": {
                           "height": "8885",
                           "round": "0",
                           "step": 1,
                           "start_time": "2019-11-12T03:10:32.107287565Z",
                           "proposal": false,
                           "proposal_block_parts_header": {
                             "total": "0",
                             "hash": ""
                           },
                           "proposal_block_parts": null,
                           "proposal_pol_round": "-1",
                           "proposal_pol": "__",
                           "prevotes": "__",
                           "precommits": "__",
                           "last_commit_round": "0",
                           "last_commit": "xx",
                           "catchup_commit_round": "-1",
                           "catchup_commit": "__"
                         },
                         "stats": {
                           "votes": "966",
                           "block_parts": "78"
                         }
                       }
                     },
                     {
                       "node_address": "fe8461d424b60b07d23a55a3906e848bcaa7a42d@192.168.1.147:37816",
                       "peer_state": {
                         "round_state": {
                           "height": "8885",
                           "round": "0",
                           "step": 1,
                           "start_time": "2019-11-12T03:10:32.119596915Z",
                           "proposal": false,
                           "proposal_block_parts_header": {
                             "total": "0",
                             "hash": ""
                           },
                           "proposal_block_parts": null,
                           "proposal_pol_round": "-1",
                           "proposal_pol": "__",
                           "prevotes": "__",
                           "precommits": "__",
                           "last_commit_round": "0",
                           "last_commit": "xx",
                           "catchup_commit_round": "-1",
                           "catchup_commit": "__"
                         },
                         "stats": {
                           "votes": "659",
                           "block_parts": "76"
                         }
                       }
                     },
                     {
                       "node_address": "8f575bcf0cbde2a00df802bd22e2884ef7b95c31@192.168.1.145:48536",
                       "peer_state": {
                         "round_state": {
                           "height": "8885",
                           "round": "0",
                           "step": 1,
                           "start_time": "2019-11-12T03:10:31.903956914Z",
                           "proposal": false,
                           "proposal_block_parts_header": {
                             "total": "0",
                             "hash": ""
                           },
                           "proposal_block_parts": null,
                           "proposal_pol_round": "-1",
                           "proposal_pol": "__",
                           "prevotes": "__",
                           "precommits": "__",
                           "last_commit_round": "0",
                           "last_commit": "xx",
                           "catchup_commit_round": "-1",
                           "catchup_commit": "__"
                         },
                         "stats": {
                           "votes": "946",
                           "block_parts": "81"
                         }
                       }
                     },
                     {
                       "node_address": "72d73dd17c43e9d78d952a4e5d5b79402507282a@192.168.1.127:47596",
                       "peer_state": {
                         "round_state": {
                           "height": "8885",
                           "round": "0",
                           "step": 1,
                           "start_time": "2019-11-12T03:10:32.119758316Z",
                           "proposal": false,
                           "proposal_block_parts_header": {
                             "total": "0",
                             "hash": ""
                           },
                           "proposal_block_parts": null,
                           "proposal_pol_round": "-1",
                           "proposal_pol": "__",
                           "prevotes": "__",
                           "precommits": "__",
                           "last_commit_round": "0",
                           "last_commit": "xx",
                           "catchup_commit_round": "-1",
                           "catchup_commit": "__"
                         },
                         "stats": {
                           "votes": "0",
                           "block_parts": "0"
                         }
                       }
                     },
                     {
                       "node_address": "70eb2f1bc5393396d677b5f86a0f999da51c816c@192.168.1.144:41666",
                       "peer_state": {
                         "round_state": {
                           "height": "8885",
                           "round": "0",
                           "step": 1,
                           "start_time": "2019-11-12T03:10:32.088836027Z",
                           "proposal": false,
                           "proposal_block_parts_header": {
                             "total": "0",
                             "hash": ""
                           },
                           "proposal_block_parts": null,
                           "proposal_pol_round": "-1",
                           "proposal_pol": "__",
                           "prevotes": "__",
                           "precommits": "__",
                           "last_commit_round": "0",
                           "last_commit": "xx",
                           "catchup_commit_round": "-1",
                           "catchup_commit": "__"
                         },
                         "stats": {
                           "votes": "987",
                           "block_parts": "78"
                         }
                       }
                     },
                     {
                       "node_address": "11df5b88c1dc6de8f90e396f52d02d32f7a0899d@192.168.1.142:38864",
                       "peer_state": {
                         "round_state": {
                           "height": "8885",
                           "round": "0",
                           "step": 1,
                           "start_time": "2019-11-12T03:10:32.108466981Z",
                           "proposal": false,
                           "proposal_block_parts_header": {
                             "total": "0",
                             "hash": ""
                           },
                           "proposal_block_parts": null,
                           "proposal_pol_round": "-1",
                           "proposal_pol": "__",
                           "prevotes": "__",
                           "precommits": "__",
                           "last_commit_round": "0",
                           "last_commit": "xx",
                           "catchup_commit_round": "-1",
                           "catchup_commit": "__"
                         },
                         "stats": {
                           "votes": "1008",
                           "block_parts": "78"
                         }
                       }
                     },
                     {
                       "node_address": "9a0862252cfd532f027feadffbdea076b0072367@192.168.1.146:56036",
                       "peer_state": {
                         "round_state": {
                           "height": "8885",
                           "round": "0",
                           "step": 1,
                           "start_time": "2019-11-12T03:10:32.114840028Z",
                           "proposal": false,
                           "proposal_block_parts_header": {
                             "total": "0",
                             "hash": ""
                           },
                           "proposal_block_parts": null,
                           "proposal_pol_round": "-1",
                           "proposal_pol": "__",
                           "prevotes": "__",
                           "precommits": "__",
                           "last_commit_round": "0",
                           "last_commit": "xx",
                           "catchup_commit_round": "-1",
                           "catchup_commit": "__"
                         },
                         "stats": {
                           "votes": "0",
                           "block_parts": "0"
                         }
                       }
                     }
                   ]
                 }
               }
             
---
 * <span id = "strategy">tri_event_query</span>

    * @apiName：http://192.168.1.141:46657/tri_event_query

    * @api：{get}

    * @apiParam:
   
    * @apiSuccessExample Success-Response::

               {
                 "jsonrpc": "2.0",
                 "id": "",
                 "result": [
                   {
                     "timestamp": "1573285837",
                     "type": "1"
                   },
                   {
                     "timestamp": "1573523482",
                     "type": "2"
                   }
                 ]
               }

---
 * <span id = "strategy">tri_first_block</span>

    * @apiName：http://192.168.1.141:46657/tri_first_block

    * @api：{get}

    * @apiParam:
   
    * @apiSuccessExample Success-Response::
    
                {
              "jsonrpc": "2.0",
              "id": "",
              "result": {
                "genesis": {
                  "genesis_time": "2019-08-28T10:31:06.328205413Z",
                  "chain_id": "test-chain-rx2wEB",
                  "consensus_params": {
                    "block": {
                      "max_bytes": "22020096",
                      "max_gas": "-1",
                      "time_iota_ms": "1000"
                    },
                    "evidence": {
                      "max_age": "100000"
                    },
                    "validator": {
                      "pub_key_types": [
                        "ed25519"
                      ]
                    }
                  },
                  "validators": [
                    {
                      "address": "881F5463E5CB4276FF71A229B53072CC0213DF2B",
                      "pub_key": {
                        "type": "tendermint/PubKeyEd25519",
                        "value": "R00Mp/3CaLbOvMiCHZRxLVSha+o+RAMGynMz81BF0Uo="
                      },
                      "power": "10",
                      "name": ""
                    }
                  ],
                  "app_hash": ""
                }
              }
            }
---
 * <span id = "strategy">tri_num_unconfirmed_txs</span>

    * @apiName：http://192.168.1.141:46657/tri_num_unconfirmed_txs

    * @api：{get}

    * @apiParam:
   
    * @apiSuccessExample Success-Response::
    
                {
              "jsonrpc": "2.0",
              "id": "",
              "result": {
                "n_txs": "0",
                "total": "0",
                "total_bytes": "0",
                "txs": null
              }
            }

---
 * <span id = "strategy">tri_clean_unconfirmed_txs</span>

    * @apiName：http://192.168.1.141:46657/tri_clean_unconfirmed_txs

    * @api：{get}

    * @apiParam:
   
    * @apiSuccessExample Success-Response::
    
    
---
 * <span id = "strategy">tri_unconfirmed_txs</span>

    * @apiName：http://192.168.1.141:46657/tri_unconfirmed_txs

    * @api：{get}

    * @apiParam:
   
    * @apiSuccessExample Success-Response::
    
---
## UTXO
#域名使用http://192.168.1.3:9981或者https://wallet.trias.one/utxo

 * <span id = "strategy">new_account</span>

    * @apiName：https://wallet.trias.one/utxo/new_account

    * @api：{get}

    * @apiParam:name
   
    * @apiSuccessExample Success-Response::
    
                {
                "code": "success",
                "hash": "9EF8D881741D13791F1882719191AB1182042F4B318DDA3E5BF0578FF2C45865",
                "msg": "wait a moment, the user name is being registered..."
            }

 * <span id = "strategy">get_account</span>

    * @apiName：https://wallet.trias.one/utxo/get_account

    * @api：{get}

    * @apiParam:name
   
    * @apiSuccessExample Success-Response::
    
    
---

 * <span id = "strategy">get_accounts</span>

    * @apiName：https://wallet.trias.one/utxo/get_accounts

    * @api：{get}

    * @apiParam:
   
    * @apiSuccessExample Success-Response::
    
                {
                "accounts": [
                    "4tUJ9wfxPrQkwJQN37jSGF3fKHBXN4NHiNBg91USM8x7vaJ7Np8yA9466B63qpu3m3DmX75iAeHCpn2zePivCJjD",
                    "8JCoUWM73aETjg4WbxKfrTTZJua1jbdVZEpZd3G971g6oVBST2JG2KHCQVKCy8H1oZ8iEzQ9Rx3HY3Y25N3smqi",
                    "b2n6mUKSGi8Uucs5smzAWg6cq7LEs9V3Jyhb7hpHDsf3Uv5o8e5oDJRo7Hsx9vpBX7USykiAsbKHLaYxvTNEueC",
                    "63ZSVTVigbfWbUrDPuWmSbcXNqtiLm9JQAihAeyxEH1GDqsX8CTJE1V2s4WmkjZQAuYRwAfkQCvifXk6Jm8sNvTx",
                    "2ENp8uGHrS4xwf6JgUvMahsWnSUGXEep9imDdQmFxh5sFMXyyZ3zikVAqDGxU5tTEqT6BiycvTGUpwPHvSzSjfNR",
                    "2JNhZnu5NN5zCkQsY5GTZ6BHmprDD6i5HF6VqtyhFChHmzqKkpcjwJ3eiX5CqPs2L1jtA4YAXEniuYnVon2Hr5xy",
                    "3WyKwNNNzHG6kVCX8M7zpw3dc8Fc9WQMUsc6w4NSt4gKT3c4Xg5JNywgPqFjtmN8xQPZSWEmj2mGNKyMAQa3vGte"
                ],
                "code": "success"
            }

---
* <span id = "strategy">new_coinbase_tx</span>

    * @apiName：https://wallet.trias.one/utxo/new_coinbase_tx

    * @api：{post}

    * @apiParam:
   
    * @apiSuccessExample Success-Response::
    
---
* <span id = "strategy">get_balance</span>

    * @apiName：https://wallet.trias.one/utxo/get_balance

    * @api：{post}

    * @apiParam:address
    
    * @apiParam:price
   
    * @apiSuccessExample Success-Response::
    
                {
                "balance": 0,
                "balance_hide_amount": [],
                "code": "success",
                "crypto_balance": 0,
                "crypto_balance_hide_amount": []
            }
            {
                "balance": 10000000000000000030,
                "balance_hide_amount": [
                    "049dc5bd8fe7d36ecca577b47400429131a07482e8098005af91a18eaca7d0935a917decf2bbddff872cfb3332ca7ddf2eca278a3f394bedc2a8ca18d126ba892ff5e09d0e28235b0d84251e33c2f7655e516628340119c6fdce5caee982909bf31a5ebee05e654bc53e191703d41450420022fc6b530b76d3c25906524e66a5d6c03c120243",
                       "0421a45d05b5d87d506c31ae84b5e0ae71d49ff702e95a1f1ec772fc282b468912814afc486c311ff421848fc9fd59f666e839bfbcf0b9356482b21355f10c61a73f510f45bf3212c54fa64541f5a4c8431b430e3c98a9b4e4e938f7ffac6724eebd75312a16a76422a065e376d07d984b36dfa9e17f22f32f60328f1a33e7787bc690f4e585"
                ],
                "code": "success",
                "crypto_balance": 0,
                "crypto_balance_hide_amount": []
            }
---
* <span id = "strategy">new_utxo_transaction</span>

    * @apiName：https://wallet.trias.one/utxo/new_utxo_transaction

    * @api：{post}

    * @apiParam:from_address
    
    * @apiParam:to_address
    
    * @apiParam:amount
   
    * @apiSuccessExample Success-Response::

---
* <span id = "strategy">find_all_spendable_outputs</span>

    * @apiName：https://wallet.trias.one/utxo/find_all_spendable_outputs

    * @api：{get}

    * @apiParam:from_address
    
    * @apiParam:priva
   
    * @apiSuccessExample Success-Response::
    
                {
                "accumulated": 0,
                "code": "success",
                "msg": "",
                "unspent_outs": {
                    "32ADA4F4BFCDF06F48C4382BE39E63218F16BF7D": [
                        {
                            "addr": "53tCjH1GQf7rd4akqC7ayZnFkJP9Nvappym6w29jyxdzjdYQEUbVTUHDsErBjDhvtTET5QeACgNuD1mCANEYhRGW",
                            "index": 0,
                            "shield_pkey": "",
                            "value": 10000000000000000000,
                            "value_encrypt": ""
                        }
                    ],
                    "57C71DE2AD84A9745EFF26C9F8695F9202EE1C17": [
                        {
                            "addr": "53tCjH1GQf7rd4akqC7ayZnFkJP9Nvappym6w29jyxdzjdYQEUbVTUHDsErBjDhvtTET5QeACgNuD1mCANEYhRGW",
                            "index": 0,
                            "shield_pkey": "",
                            "value": "66397e397f56dde0328be82ded6c537d56397a71912b785200fc9f19a557cbf0",
                            "value_encrypt": "0421a45d05b5d87d506c31ae84b5e0ae71d49ff702e95a1f1ec772fc282b468912814afc486c311ff421848fc9fd59f666e839bfbcf0b9356482b21355f10c61a73f510f45bf3212c54fa64541f5a4c8431b430e3c98a9b4e4e938f7ffac6724eebd75312a16a76422a065e376d07d984b36dfa9e17f22f32f60328f1a33e7787bc690f4e585"
                        }
                    ],
                    "7B4C336BACA34557D148A5B167EF2ED6C003436E": [
                        {
                            "addr": "53tCjH1GQf7rd4akqC7ayZnFkJP9Nvappym6w29jyxdzjdYQEUbVTUHDsErBjDhvtTET5QeACgNuD1mCANEYhRGW",
                            "index": 0,
                            "shield_pkey": "",
                            "value": 10,
                            "value_encrypt": ""
                        }
                    ],
                    "7C5BF278E38A0FA9C10E296191EADFD572E2F8EF": [
                        {
                            "addr": "53tCjH1GQf7rd4akqC7ayZnFkJP9Nvappym6w29jyxdzjdYQEUbVTUHDsErBjDhvtTET5QeACgNuD1mCANEYhRGW",
                            "index": 0,
                            "shield_pkey": "",
                            "value": "76913dc7284abac0b1db00384ca95defe320bf25718f15dc53e9a5d0da13de86",
                            "value_encrypt": "049dc5bd8fe7d36ecca577b47400429131a07482e8098005af91a18eaca7d0935a917decf2bbddff872cfb3332ca7ddf2eca278a3f394bedc2a8ca18d126ba892ff5e09d0e28235b0d84251e33c2f7655e516628340119c6fdce5caee982909bf31a5ebee05e654bc53e191703d41450420022fc6b530b76d3c25906524e66a5d6c03c120243"
                        }
                    ],
                    "887CA1DD02522409EAF669EA4478B8A0AE4BD47F": [
                        {
                            "addr": "53tCjH1GQf7rd4akqC7ayZnFkJP9Nvappym6w29jyxdzjdYQEUbVTUHDsErBjDhvtTET5QeACgNuD1mCANEYhRGW",
                            "index": 0,
                            "shield_pkey": "",
                            "value": 10,
                            "value_encrypt": ""
                        }
                    ],
                    "9A14A923044A895EDE340C7B91B462FF0140B32D": [
                        {
                            "addr": "53tCjH1GQf7rd4akqC7ayZnFkJP9Nvappym6w29jyxdzjdYQEUbVTUHDsErBjDhvtTET5QeACgNuD1mCANEYhRGW",
                            "index": 0,
                            "shield_pkey": "",
                            "value": 10,
                            "value_encrypt": ""
                        }
                    ],
                    "ACDD2B6B93669A8BEE638C0ECCBFCB1BD7C32EEA": [
                        {
                            "addr": "bed7d3b9cbfce2c9ef8b7cfdc70e64d04f44e0ee2ef3be03e97cdad8ba2c9147",
                            "index": 1,
                            "shield_pkey": "ea58a7780f197806edaa1e3d415bcc60b1da205fc35c1a1c4da27cb3b443aac3dd29e798e27bd5932f8aa9295dc9042ac75b502f5467f3fce95d6217fcdd430d",
                            "value": 95000000000000000000,
                            "value_encrypt": ""
                        }
                    ]
                }
            }

---
* <span id = "strategy">broadcast_tx</span>

    * @apiName：https://wallet.trias.one/utxo/broadcast_tx

    * @api：{post}

    * @apiParam:tx
   
    * @apiSuccessExample Success-Response::
    

---
* <span id = "strategy">get_prove_data</span>

    * @apiName：https://wallet.trias.one/utxo/get_prove_data

    * @api：{post}

    * @apiParam:参数为数组形式的body data
   
    * @apiSuccessExample Success-Response::
    
               {
                   "code": "success",
                   "content": "[\"30203632353435333038313738393137353737383837303431393631383433333133363034363238343035373339353135323531303331313432313936353536383335323439373037313330383020312030203334303033343438303238323234363434313130373034343037343237343932333838363739353534373039393139333734373534373539333931333231313338323535363632333530353920300A30203434393631333131323236353238333132333538373936323038393634393935303139373639393834353137363538333237373336383837363734353637343337383738323239323134303820393433353938363039333030373432393031363136303937373032373630383332353639393237373036393339383839303734333736353937323135383235333638383639383238383239322031203020313436343433363934303233333830323037303431303538303837393939373238303938333632303335393832343337373337373835333035363236303938363238363236343930343134313620300A30203132363830333634373830303633363934313835363739383037353430363731343732303737303539373633393438323232333634393230313635383639343830383739383136353333313720312030203530303439343636373539343330373734393432373630383235363237313234383239303933303433333035393936373938303139383135343737393436323934333839313537363934323020300A30203438343539383937383033373337373332303633313230373337393039313330383634343037353734343039393535383739313535383435393539353732343636363636373538373132303520300A30203937373830363735333030333235393433343839333834303732373537383631383237393236373333353936393934313936393036343539333530343334323532373231393930343131393620300A\",\"e38990d0c7fc009880a9c07c23842e886c6bbdc964ce6bdd5817ad357335ee6f\",\"d1ec675902ef1633427ca360b290b0b3045a0d9058ddb5e648b4c3c3224c5c68\"]",
                   "msg": ""
               }

---
* <span id = "strategy">get_address_tx</span>

    * @apiName：https://wallet.trias.one/utxo/get_address_tx

    * @api：{get}

    * @apiParam:address
    
    * @apiParam:priva
   
    * @apiSuccessExample Success-Response::
    
            {
                "txs": [
                    {
                        "amount": "76913dc7284abac0b1db00384ca95defe320bf25718f15dc53e9a5d0da13de86",
                        "from": "YVdtnuhpupvfnVWzk7ZFtR2jhxeJxTDikAoNrvqggnpQo2j9kcUGb71LeXDvrsQAMc4LF7U2VVwDjAW6nTTLtXH",
                        "is_anonymous": false,
                        "timestamp": 1572320646007,
                        "to": "53tCjH1GQf7rd4akqC7ayZnFkJP9Nvappym6w29jyxdzjdYQEUbVTUHDsErBjDhvtTET5QeACgNuD1mCANEYhRGW",
                        "tx_id": "7C5BF278E38A0FA9C10E296191EADFD572E2F8EF",
                        "type": "receive"
                    },
                    {
                        "amount": 10000000000000000000,
                        "from": "YVdtnuhpupvfnVWzk7ZFtR2jhxeJxTDikAoNrvqggnpQo2j9kcUGb71LeXDvrsQAMc4LF7U2VVwDjAW6nTTLtXH",
                        "is_anonymous": false,
                        "timestamp": 1572320730049,
                        "to": "53tCjH1GQf7rd4akqC7ayZnFkJP9Nvappym6w29jyxdzjdYQEUbVTUHDsErBjDhvtTET5QeACgNuD1mCANEYhRGW",
                        "tx_id": "32ADA4F4BFCDF06F48C4382BE39E63218F16BF7D",
                        "type": "receive"
                    },
                    {
                        "amount": 10,
                        "from": "2wr1S4th8nWU3938q2RUdLMu5jjTLZUQwNfBH5o4XqW5UP79hp8xZKtcCjxMDPLZNfM1zEFEYTNkn27Li7DDkCsG",
                        "is_anonymous": false,
                        "timestamp": 1572421066120,
                        "to": "53tCjH1GQf7rd4akqC7ayZnFkJP9Nvappym6w29jyxdzjdYQEUbVTUHDsErBjDhvtTET5QeACgNuD1mCANEYhRGW",
                        "tx_id": "9A14A923044A895EDE340C7B91B462FF0140B32D",
                        "type": "receive"
                    },
                    {
                        "amount": 10,
                        "from": "2wr1S4th8nWU3938q2RUdLMu5jjTLZUQwNfBH5o4XqW5UP79hp8xZKtcCjxMDPLZNfM1zEFEYTNkn27Li7DDkCsG",
                        "is_anonymous": false,
                        "timestamp": 1572506405545,
                        "to": "53tCjH1GQf7rd4akqC7ayZnFkJP9Nvappym6w29jyxdzjdYQEUbVTUHDsErBjDhvtTET5QeACgNuD1mCANEYhRGW",
                        "tx_id": "887CA1DD02522409EAF669EA4478B8A0AE4BD47F",
                        "type": "receive"
                    },
                    {
                        "amount": 10,
                        "from": "2wr1S4th8nWU3938q2RUdLMu5jjTLZUQwNfBH5o4XqW5UP79hp8xZKtcCjxMDPLZNfM1zEFEYTNkn27Li7DDkCsG",
                        "is_anonymous": false,
                        "timestamp": 1572506523456,
                        "to": "53tCjH1GQf7rd4akqC7ayZnFkJP9Nvappym6w29jyxdzjdYQEUbVTUHDsErBjDhvtTET5QeACgNuD1mCANEYhRGW",
                        "tx_id": "7B4C336BACA34557D148A5B167EF2ED6C003436E",
                        "type": "receive"
                    },
                    {
                        "amount": "66397e397f56dde0328be82ded6c537d56397a71912b785200fc9f19a557cbf0",
                        "from": "QXtE2TsRx6kYcsLh7rBJXApRCywmCoUKx2sYM9pbBTD2HkHpwvF69M4W2bWErTA7FK4uFuSsEpTveKqDshBVvrS",
                        "is_anonymous": false,
                        "timestamp": 1573203203724,
                        "to": "53tCjH1GQf7rd4akqC7ayZnFkJP9Nvappym6w29jyxdzjdYQEUbVTUHDsErBjDhvtTET5QeACgNuD1mCANEYhRGW",
                        "tx_id": "57C71DE2AD84A9745EFF26C9F8695F9202EE1C17",
                        "type": "receive"
                    },
                    {
                        "amount": 100000000000000000000,
                        "from": "mine",
                        "is_anonymous": true,
                        "shield_pkey": "39276fd3235f0ec507c05c148c2332bc7cbd6b80246f39510250671c75b6c2213f2cf00198f412d1a9c9f232fb6891196ab1121bb047244fccb0d3d783fa2003",
                        "timestamp": 1572422456513,
                        "to": "0210f9933f780e36e8bbc42686619b1f173daa51e627760784fcfc5713c3cf1f",
                        "tx_id": "114C32B0B0584AD030984AE0D50C55C8D0D1E7EE",
                        "type": "receive"
                    },
                    {
                        "amount": 5000000000000000000,
                        "from": "0210f9933f780e36e8bbc42686619b1f173daa51e627760784fcfc5713c3cf1f",
                        "is_anonymous": true,
                        "timestamp": 1572422530546,
                        "to": "70d1ccc4b6a146358fed6b62b89aca557d555f2ed5e0f0148ecf8d097dc4aa08",
                        "tx_id": "ACDD2B6B93669A8BEE638C0ECCBFCB1BD7C32EEA",
                        "type": "send"
                    }
                ]
            }

---
* <span id = "strategy">get_latest_block_height</span>

    * @apiName：https://wallet.trias.one/utxo/get_latest_block_height

    * @api：{get}

    * @apiParam:
   
    * @apiSuccessExample Success-Response::
    
            {
                "height": 0,
                "latest_block_height": "170703"
            }

---
## Attestation

* <span id = "strategy">getranking</span>

    * @apiName：http//:192.168.1.3:8987/trias/getranking

    * @api：{get}

    * @apiParam:
   
    * @apiSuccessExample Success-Response::
    
            [
              {
                "attestee": "192.168.1.142", 
                "score": 0.21045008
              }, 
              {
                "attestee": "192.168.1.143", 
                "score": 0.170164
              }, 
              {
                "attestee": "192.168.1.146", 
                "score": 0.15255627
              }, 
              {
                "attestee": "192.168.1.144", 
                "score": 0.14096914
              }, 
              {
                "attestee": "192.168.1.147", 
                "score": 0.12405991
              }, 
              {
                "attestee": "192.168.1.145", 
                "score": 0.10894079
              }, 
              {
                "attestee": "192.168.1.141", 
                "score": 0.09285981
              }
            ]


---
* <span id = "strategy">getverifynodes</span>

    * @apiName：http//:192.168.1.3:8987/trias/getverifynodes

    * @api：{get}

    * @apiParam:
   
    * @apiSuccessExample Success-Response::
    
---
* <span id = "strategy">getdistrustfulnodes</span>

    * @apiName：http//:192.168.1.3:8987/trias/getdistrustfulnodes

    * @api：{get}

    * @apiParam:
   
    * @apiSuccessExample Success-Response::
    
---
## StreamNet

* <span id = "strategy">QueryNodes</span>

    * @apiName：http//:192.168.1.141:8000/QueryNodes

    * @api：{post}

    * @apiParam: period:1       参数为1代表最新的数据
    
    * @apiParam:numRank
    
    @apiExample 
     curl -s -X POST http://192.168.1.141:8000/QueryNodes -H 'Content-Type:application/json' -H 'cache-control: no-cache' -d "{\"period\":-1,\"numRank\":100}"

   
    * @apiSuccessExample Success-Response::
    
    
                {
               "Code": 1,
               "Message": "Query node data successfully",
               "Data": {
                  "DataScore": [{
                     "attestee": "192.168.1.141",
                     "score": 0.18971772
                  }, {
                     "attestee": "192.168.1.145",
                     "score": 0.17339469
                  }, {
                     "attestee": "192.168.1.142",
                     "score": 0.16059442
                  }, {
                     "attestee": "192.168.1.144",
                     "score": 0.12110464
                  }, {
                     "attestee": "192.168.1.143",
                     "score": 0.11414328
                  }, {
                     "attestee": "192.168.1.147",
                     "score": 0.08592692
                  }, {
                     "attestee": "192.168.1.146",
                     "score": 0.08011833
                  }, {
                     "attestee": "5",
                     "score": 0.01071429
                  }, {
                     "attestee": "3",
                     "score": 0.01071429
                  }, {
                     "attestee": "7",
                     "score": 0.01071429
                  }, {
                     "attestee": "2",
                     "score": 0.01071429
                  }, {
                     "attestee": "1",
                     "score": 0.01071429
                  }, {
                     "attestee": "4",
                     "score": 0.01071429
                  }, {
                     "attestee": "6",
                     "score": 0.01071429
                  }],
                  "DataCtx": [{
                     "attester": "192.168.1.141",
                     "attestee": "192.168.1.141",
                     "score": 1
                  }, {
                     "attester": "192.168.1.144",
                     "attestee": "192.168.1.145",
                     "score": 4
                  }, {
                     "attester": "192.168.1.143",
                     "attestee": "192.168.1.142",
                     "score": 3
                  }, {
                     "attester": "192.168.1.147",
                     "attestee": "192.168.1.144",
                     "score": 7
                  }, {
                     "attester": "192.168.1.146",
                     "attestee": "192.168.1.143",
                     "score": 6
                  }, {
                     "attester": "192.168.1.142",
                     "attestee": "192.168.1.147",
                     "score": 2
                  }, {
                     "attester": "192.168.1.144",
                     "attestee": "192.168.1.146",
                     "score": 4
                  }]
               }
            }


---
* <span id = "strategy">AddNode</span>

    * @apiName：http//:192.168.1.141:8000/AddNode

    * @api：{get}

    * @apiParam:
    
    * @apiParam:numRank
    
    @apiExample 
     curl -s -X POST http://127.0.0.1:8000/AddNode -H 'Content-Type:application/json' -H 'cache-control: no-cache' -d "{\"Attester\":\"192.168.1.142\",\"Attestee\":\"192.168.1.141\",\"Score\":1}"

   
    * @apiSuccessExample Success-Response::
    
                {
               "Code": 1,
               "Message": "Node added successfully",
               "Data": null
            }
---
* <span id = "strategy">getDagMap</span>

    * @apiName：http://13.250.111.23/streamnet-api/getDagMap

    * @api：{get}

    * @apiParam:
    
    * @apiParam:numRank
    
    * @apiSuccessExample Success-Response::
    
                {
               "code": 1,
               "message": "success",
               "data": [{
                  "source": "NSDOLA",
                  "target": "BJUQ9T"
               }, {
                  "source": "BJUQ9T",
                  "target": "EGSSMC"
               }, {
                  "source": "BJUQ9T",
                  "target": "W9ASCQ"
               }, {
                  "source": "XWCGMN",
                  "target": "NSDOLA"
               }]
            }

    
