import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FineLeafComponent } from './fine-leaf.component';

describe('FineLeafComponent', () => {
  let component: FineLeafComponent;
  let fixture: ComponentFixture<FineLeafComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FineLeafComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FineLeafComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
