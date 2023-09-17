export default class Car {
    constructor(brand, motor, color) {
      this.brand = brand;
      this.motor = motor;
      this.color = color;
    }
  
    cloneCar() {
      return new Car(this.brand, this.motor, this.color);
    }
  }
  
  const tc1 = new Car("Nissan", "Turbo", "Pink");
  const tc2 = tc1.cloneCar();
  
  console.log(tc1);
  console.log(tc1 instanceof Car);
  
  console.log(tc2);
  console.log(tc2 instanceof Car);
  
  console.log(tc1 === tc2);
