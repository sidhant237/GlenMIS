import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PluckingComponent } from './plucking.component';

describe('PluckingComponent', () => {
  let component: PluckingComponent;
  let fixture: ComponentFixture<PluckingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PluckingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PluckingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
