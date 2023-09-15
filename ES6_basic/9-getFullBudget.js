//import
import getBudgetObject from './7-getBudgetObject.js';


export default function getFullBudgetObject(income, gdp, capita) {
  const baseBudget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...baseBudget,
    getIncomeInDollars: (incomeValue) => `$${incomeValue}`,
    getIncomeInEuros: (incomeValue) => `${incomeValue} euros`,
  };

  return fullBudget;
}
