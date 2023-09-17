export default class Building {
    constructor(sqft) {
      this._sqft = sqft;
      if (this.constructor === Building) {
        throw new Error('Abstract class Building cannot be instantiated');
      }
      if (typeof this.evacuationWarningMessage !== 'function') {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
    }
  
    get sqft() {
      return this._sqft;
    }
  }
