import allure


class Test_002:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("第一步")
    def test_001(self):
        print("\n test001")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_002(self):
        print("\n test002")

    @allure.severity(allure.severity_level.NORMAL)
    def test_003(self):
        assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_004(self):
        print("\n test004")

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_005(self):
        print("\n test005")
