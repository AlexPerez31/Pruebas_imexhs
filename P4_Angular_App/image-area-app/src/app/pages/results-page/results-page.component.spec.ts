import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResultsPageComponent } from './results-page.component';

describe('ResultsPageComponent', () => {
  let component: ResultsPageComponent;
  let fixture: ComponentFixture<ResultsPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ResultsPageComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ResultsPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should return 5 items per page from getPageData', () => {
    const data = new Array(10).fill({ area: 42 });
    const pageData = component.getPageData(data);
    expect(pageData.length).toBe(5);
  });
});
