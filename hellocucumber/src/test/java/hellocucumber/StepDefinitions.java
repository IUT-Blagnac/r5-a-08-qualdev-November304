package hellocucumber;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class StepDefinitions {

    @Given("an example scenario")
    public void anExampleScenario() {
    }

    @When("all step definitions are implemented")
    public void allStepDefinitionsAreImplemented() {
    }

    @Then("the scenario passes")
    public void theScenarioPasses() {
    }

    @Given("today is {string}")
    public void today_is(String string) {
        IsItFriday.day = string;
    }
    @When("I ask whether it's Friday yet")
    public void i_ask_whether_it_s_friday_yet() {
        IsItFriday.isDayFriday = IsItFriday.isItFriday(IsItFriday.day);
    }
    @Then("I should be told {string}")
    public void i_should_be_told(String string) {
        assert IsItFriday.isDayFriday.equals(string);
    }

}

class IsItFriday {

    static String day;

    static String isItFriday(String today) {
        if(today.equals("Friday")) {
            return "TGIF";
        }
        return "Nope";
    }

    static String isDayFriday;
}
