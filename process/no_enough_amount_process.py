#coding=utf-8
import unittest
from case.creat_wallet import CreatWallet
from case.get_coin import GetCoin
from case.get_hidden_coin import GetHiddenCoin
from case.no_enough_public_address_hidden_amount import NoEnoughPublicAddressHiddenAmount
from case.check_view_account_info import CheckViewAccountInfo
import time,os,HTMLTestReportCN
class WebWalletProcess(unittest.TestCase):
    def setUp(self):
        pass
    def test_0creat_wallet(self):
        CreatWallet().creat_wallet()
        CreatWallet().creat_wallet()

    def test_1getcoin(self):
        GetCoin().getcoin()
        GetHiddenCoin().get_hidden_coin()

    def test_2check_view_account_info(self):
        CheckViewAccountInfo().check_view_account_info()

    def test_2no_enough_public_address_hidden_amount(self):
        NoEnoughPublicAddressHiddenAmount().no_enough_public_address_hidden_amount()

    def tearDown(self):
        pass

if __name__ == '__main__':
    now_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    qian = os.path.abspath('.').split('process')[0]
    # Define a report store path
    filename = qian + 'report' + '\\' + now_time + 'result.html'
    fp = open(filename, 'wb')

    testsuite=unittest.TestSuite()
    testsuite.addTest(WebWalletProcess('test_0creat_wallet'))
    testsuite.addTest(WebWalletProcess('test_1getcoin'))
    testsuite.addTest(WebWalletProcess('test_2no_enough_public_address_hidden_amount'))
    runner=HTMLTestReportCN.HTMLTestRunner(

        stream=fp,
        title=u'web wallet process,',
        description=u'case execution'
    )
        # Run the test case
    runner.run(testsuite)

    fp.close()