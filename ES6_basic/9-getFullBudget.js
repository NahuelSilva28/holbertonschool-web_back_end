import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const baseBudget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...baseBudget,
    getIncomeInDollars: (incomeInDollars) => `$${incomeInDollars}`,
    getIncomeInEuros: (incomeInEuros) => `${incomeInEuros} euros`,
  };

  return fullBudget;
}
