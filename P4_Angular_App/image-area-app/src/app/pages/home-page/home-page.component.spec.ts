import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HomePageComponent } from './home-page.component';

describe('HomePageComponent', () => {
  let component: HomePageComponent;
  let fixture: ComponentFixture<HomePageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HomePageComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HomePageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  // Verifique que el valor inicial de puntos sea 1000
  it('should initialize points to 1000', () => {
    expect(component.points).toBe(1000);
  });

  // Verifique que se ejecute el evento al calcular el área si hay imagen cargada
  it('should emit goToResults when calculateArea is called with an image', () => {
    component.imageSrc = 'data:image/png;base64,...'; // simulamos que hay una imagen
    spyOn(component.goToResults, 'emit'); // espía el método emit
    component.calculateArea(); // llamamos al método
    expect(component.goToResults.emit).toHaveBeenCalled(); // verificamos que se llamó
  });
});