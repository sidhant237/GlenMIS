import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CultivationComponent } from './cultivation.component';

describe('CultivationComponent', () => {
  let component: CultivationComponent;
  let fixture: ComponentFixture<CultivationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CultivationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CultivationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
