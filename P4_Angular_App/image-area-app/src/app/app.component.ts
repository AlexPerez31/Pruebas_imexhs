import { Component } from '@angular/core';
import { HomePageComponent } from './pages/home-page/home-page.component';
import { ResultsPageComponent } from './pages/results-page/results-page.component';
import { MatTabsModule } from '@angular/material/tabs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  standalone: true,
  // Aquí importé los componentes que estan en cada modulo y las tabs
  imports: [HomePageComponent, ResultsPageComponent, MatTabsModule],
})
export class AppComponent {
  selectedTabIndex = 0;
}
