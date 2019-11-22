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
目录

1\. 查询指定项目属性接口

---

**1\. 查询指定项目属性**
###### 接口功能
> 获取制定项目的分类信息

###### URL
> [http://www.api.com/index.php](www.api.com/index.php)

###### 支持格式
> JSON

###### HTTP请求方式
> GET

###### 请求参数
> |参数|必选|类型|说明|
|:-----  |:-------|:-----|-----                               |
|name    |ture    |string|请求的项目名                          |
|type    |true    |int   |请求项目的类型。1：类型一；2：类型二 。|

###### 返回字段
> |返回字段|字段类型|说明                              |
|:-----   |:------|:-----------------------------   |
|status   |int    |返回结果状态。0：正常；1：错误。   |
|company  |string | 所属公司名                      |
|category |string |所属类型                         |

###### 接口示例
> 地址：[http://www.api.com/index.php?name="可口可乐"&type=1](http://www.api.com/index.php?name="可口可乐"&type=1)
``` javascript
{
    "statue": 0,
    "company": "可口可乐",
    "category": "饮料",
}
