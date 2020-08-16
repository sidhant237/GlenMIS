import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PluckingGrpComponent } from './plucking-grp.component';

describe('PluckingGrpComponent', () => {
  let component: PluckingGrpComponent;
  let fixture: ComponentFixture<PluckingGrpComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PluckingGrpComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PluckingGrpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
