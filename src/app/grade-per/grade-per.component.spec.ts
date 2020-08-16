import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GradePerComponent } from './grade-per.component';

describe('GradePerComponent', () => {
  let component: GradePerComponent;
  let fixture: ComponentFixture<GradePerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GradePerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GradePerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
