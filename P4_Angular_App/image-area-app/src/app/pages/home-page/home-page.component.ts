import { Component, EventEmitter, Output } from '@angular/core'
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatStepperModule } from '@angular/material/stepper';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatSliderModule } from '@angular/material/slider';
import { StainService } from '../../features/image-area/stain.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css'],
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatStepperModule,
    MatButtonModule,
    MatIconModule,
    MatSliderModule,
  ],
})

export class HomePageComponent {
  // Esto es solo para cambiar de tab automaticamente
  @Output() goToResults = new EventEmitter<void>();
  // Esta propiedad la uso para guardar la imagen cargada
  imageSrc: string | ArrayBuffer | null = null;
  // Aca coloco un valor inicial de los puntos para el slider
  points = 1000;
  // Agregue esto para verificar que primero se suba la imagen antes de avanzar
  isImageLoaded = false;
  // Aca alamceno el area calculada
  calculatedArea: number | null = null;
  // Aca llamo al servicio que cree para calcular la imagen
  constructor(private stainService: StainService) {}

  // Esta función se ejecuta cuando el usuario selecciona una imagen 
  onImageSelected(event: Event) {
    const file = (event.target as HTMLInputElement).files?.[0];
    if (file) {
      const reader = new FileReader(); 
      reader.onload = () => {
        // Esto lo hago para despues poderlo mostrar en un <img>
        this.imageSrc = reader.result;
        this.isImageLoaded = true;
      };

      // Hago que la imagen se guarde DataURL en base64
      reader.readAsDataURL(file);
    }
  }

  // Esta funcion envia los datos de la imagen al servicio que cree
  // No recibe los resultados porque esos iran en la otra tab
  calculateArea(): void {
    if (!this.imageSrc) {
      console.error('No se ha cargado ninguna imagen');
      return;
    }
    // Aca creo la instancia de la imagen para obtener los datos y un canvas oculto
    // para poder acceder a los pixeles y enviar todo a procesar
    const img = new Image();
    img.src = this.imageSrc as string;
    img.onload = () => {
      const canvas = document.createElement('canvas');
      canvas.width = img.width;
      canvas.height = img.height;
      const ctx = canvas.getContext('2d');
      if (!ctx) {
        console.error('No se pudo obtener el contexto del canvas');
        return;
      }
      ctx.drawImage(img, 0, 0);
      const imageData = ctx.getImageData(0, 0, img.width, img.height);
      // Aca envio la imagen al servicio
      this.stainService.calculateStainArea(
        this.imageSrc as string,
        imageData,
        img.width,
        img.height,
        this.points
      );
    };
    img.onerror = () => {
      console.error('Error al cargar la imagen');
    };

    this.goToResults.emit();
  }
}