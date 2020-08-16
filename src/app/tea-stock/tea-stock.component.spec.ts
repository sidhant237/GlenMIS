import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TeaStockComponent } from './tea-stock.component';

describe('TeaStockComponent', () => {
  let component: TeaStockComponent;
  let fixture: ComponentFixture<TeaStockComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TeaStockComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TeaStockComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
