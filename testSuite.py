import unittest

from byudjeetbc import budget_erbcTestCases, byudjeetbcTestCases, mainbyudjeetTestCases, mainbyudjeetzarplataTestCases, \
    vacancy_erbcTestCases

testSuite = unittest.TestSuite()
testSuite.addTests(unittest.makeSuite(byudjeetbcTestCases.ByudjeetbcTestCases))
testSuite.addTest(unittest.makeSuite(mainbyudjeetTestCases.MainbyudjeetTestCases))
testSuite.addTest(unittest.makeSuite(mainbyudjeetzarplataTestCases.MainbyudjeetzarplataTestCases))
testSuite.addTest(unittest.makeSuite(budget_erbcTestCases.Budget_erbcTestCases))
testSuite.addTest(unittest.makeSuite(vacancy_erbcTestCases.Vacancy_erbcTestCases))

testResult = unittest.TestResult()

runner = unittest.TextTestRunner(verbosity=2)
testResult = runner.run(testSuite)

print("errors")
print(len(testResult.errors))
print("failures")
print(len(testResult.failures))
print("skipped")
print(len(testResult.skipped))
print("testsRun")
print(testResult.testsRun)



