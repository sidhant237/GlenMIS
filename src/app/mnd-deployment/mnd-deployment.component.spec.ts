import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MndDeploymentComponent } from './mnd-deployment.component';

describe('MndDeploymentComponent', () => {
  let component: MndDeploymentComponent;
  let fixture: ComponentFixture<MndDeploymentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MndDeploymentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MndDeploymentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
