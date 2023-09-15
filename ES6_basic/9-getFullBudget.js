//import
import getBudgetObject from './7-getBudgetObject.js';


export default function getFullBudgetObject(income, gdp, capita) {
  const baseBudget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...baseBudget,
    getIncomeInDollars(incomeValue) {
      return `$${incomeValue}`;
    },
    getIncomeInEuros(incomeValue) {
      return `${incomeValue} euros`;
    },
  };

  return fullBudget;
}
