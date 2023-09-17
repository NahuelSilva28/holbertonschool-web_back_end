import getBudgetObject from './7-getBudgetObject';

export default function getFullBudgetObject(income, gdp, capita) {
  const baseBudget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...baseBudget,
    getIncomeInDollars: () => `$${income}`,
    getIncomeInEuros: () => `${income} euros`,
  };

  return fullBudget;
}
