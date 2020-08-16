import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CultivationGrpComponent } from './cultivation-grp.component';

describe('CultivationGrpComponent', () => {
  let component: CultivationGrpComponent;
  let fixture: ComponentFixture<CultivationGrpComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CultivationGrpComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CultivationGrpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
