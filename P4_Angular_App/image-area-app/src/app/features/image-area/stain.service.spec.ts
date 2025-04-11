import { TestBed } from '@angular/core/testing';
import { StainService } from './stain.service';

describe('StainService', () => {
  let service: StainService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(StainService);
    localStorage.clear(); //Limpio antes de hacer las pruebas
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should add a result after calculateStainArea is called', (done) => {
    const width = 10;
    const height = 10;
    const points = 100;

    // Crear imagen en blanco y negro
    const blackImageData = new ImageData(width, height);
    for (let i = 0; i < blackImageData.data.length; i += 4) {
      blackImageData.data[i] = 0;   
      blackImageData.data[i + 1] = 0; 
      blackImageData.data[i + 2] = 0; 
      blackImageData.data[i + 3] = 255; 
    }

    service.calculateStainArea('data:image/png;base64,xyz', blackImageData, width, height, points);

    service.results$.subscribe((results) => {
      expect(results.length).toBeGreaterThan(0);
      expect(results[0].width).toBe(width);
      expect(results[0].height).toBe(height);
      expect(results[0].points).toBe(points);
      done();
    });
  });
});
