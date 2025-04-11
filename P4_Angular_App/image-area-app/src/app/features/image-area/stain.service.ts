import { Injectable } from '@angular/core';
// Importé BehaviorSubject desde RxJS para manejar los estados reactivos
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class StainService {
  // En BehaviorSubject guardare el resultado del área calculada actual
  private stainAreaSubject = new BehaviorSubject<number | null>(null);

  // Esta parte la hice para avisar que se guarda algo nuevo y se pueda actualizar la pagina sin recargarla
  private resultsSubject = new BehaviorSubject<any[]>(this.loadStoredResults());
  // La declare públicamente para que los componentes puedan obtener el historial
  results$ = this.resultsSubject.asObservable();

  // Aca traigo el hostiral desde localstorage y lo carga
  private loadStoredResults(): any[] {
    const storedResults = localStorage.getItem('stainResults');
    return storedResults ? JSON.parse(storedResults) : [];
  }

  constructor() {}
  /**
   * @param imageSrc - Imagen en base64 para guardar el resultado
   * @param imageData - Aca pongo todos los datos de los pixeles de la imagen
   * @param width - El ancho de la imagen para limitar los valores x de los puntos aleatorios
   * @param height - La altura de la imagen para limitar los valores y
   * @param points - Este fue el número de puntos aleatorios que viene del slider
   */

  calculateStainArea(imageSrc: string, imageData: ImageData, width: number, height: number, points: number): void {
    // Este sera el contador de los pixeles que esten dentro de la mancha
    let pointsInside = 0;

    // Aca generé coordenadas aleatorias dentro del tamaño de la imagen
    for (let i = 0; i < points; i++) {
      const x = Math.floor(Math.random() * width);
      const y = Math.floor(Math.random() * height);
      // Calculé el índice correspondiente en el array de los píxeles y obtuve los calores del R G B
      const index = (y * width + x) * 4;
      const r = imageData.data[index];
      const g = imageData.data[index + 1];
      const b = imageData.data[index + 2];

      // Como el pixel dentro de la mancha sera negro (0, 0, 0)
      if (r === 0 && g === 0 && b === 0) {
        pointsInside++;
      }
    }

    // Aca uso la formula proporcionada 
    const totalImageArea = width * height;
    const estimatedStainArea = totalImageArea * (pointsInside / points);

    // Esta parte la hice para avisar que se guarda algo nuevo y se pueda actualizar la pagina sin recargarla
    this.stainAreaSubject.next(estimatedStainArea);

    // Esta parte la cree para guardar el resultado en localstorage,
    // asi los datos persisten si la pagina se recarga
    const result = {
        imageSrc,
        width,
        height,
        points,
        pointsInside,
        estimatedArea: estimatedStainArea,
        timestamp: new Date().toLocaleString(),
      };
  
      const storedResults = localStorage.getItem('stainResults');
      let results = storedResults ? JSON.parse(storedResults) : [];
      results.push(result);
      localStorage.setItem('stainResults', JSON.stringify(results));

    // Aca recolecto todo lo de localstorage para que la tabla pueda btenerlos sin recargar pagina
    this.resultsSubject.next(results);

  }

  resetStainArea(): void {
    this.stainAreaSubject.next(null);
  }
}