package dojo;

import java.util.ArrayList;
import java.util.List;

class Order {
    String owner;
    String target;
    List<String> cocktails = new ArrayList<>();

    public void declareOwner(String owner) {
        this.owner = owner;
    }

    public void declareTarget(String target) {
        this.target = target;
    }

    public List<String> getCocktails() {
        return cocktails;
    }
}