import { TestBed } from '@angular/core/testing';

import { DateLoaderService } from './date-loader.service';

describe('DateLoaderService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: DateLoaderService = TestBed.get(DateLoaderService);
    expect(service).toBeTruthy();
  });
});
