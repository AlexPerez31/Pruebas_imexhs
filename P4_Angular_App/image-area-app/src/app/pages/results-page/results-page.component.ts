import { Component, computed, signal, effect } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StainService } from '../../features/image-area/stain.service';

@Component({
  selector: 'app-results-page',
  templateUrl: './results-page.component.html',
  styleUrls: ['./results-page.component.css'],
  standalone: true,
  imports: [CommonModule],
})
export class ResultsPageComponent {
  // Me suscribí al observable de resultados del servicio para obtener los datos reactivos con este get
  get results$() {
    return this.stainService.results$;
  }

  // Aca quise agruegar paginacion a la tabla
  pageSize = 5;
  currentPage = 1;
  totalPages = 1;
  paginatedResults: any[] = [];

  // Aca cuando se actualizan los resultados se calcula la cantidad de paginas
  constructor(private stainService: StainService) {
    this.results$.subscribe((results) => {
      this.totalPages = Math.ceil(results.length / this.pageSize);
      this.paginatedResults = this.getPageData(results);
    });
  }
  // Esto es para mostrar los datos entre paginas
  getPageData(data: any[]): any[] {
    const start = (this.currentPage - 1) * this.pageSize;
    return data.slice(start, start + this.pageSize);
  }
  nextPage(): void {
    if (this.currentPage < this.totalPages) {
      this.currentPage++;
      this.updatePage();
    }
  }
  prevPage(): void {
    if (this.currentPage > 1) {
      this.currentPage--;
      this.updatePage();
    }
  }
  updatePage(): void {
    this.results$.subscribe((results) => {
      this.paginatedResults = this.getPageData(results);
    });
  }

  // Esto es apra limpiar el localstorage
  clearResults(): void {
    localStorage.removeItem('stainResults'); 
    this.paginatedResults = [];
    this.totalPages = 1;
    this.currentPage = 1;
    this.stainService['resultsSubject'].next([]);
  }
}
