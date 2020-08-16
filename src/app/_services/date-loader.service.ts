import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from './../../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class DateLoaderService {

  updatedDatesData = [];

  constructor(private http: HttpClient) { }

  loadUpdatedDates() {
    const url = environment.url + 'dates';
    this.http.get(url).subscribe(
      (result: any) => {
        this.updatedDatesData = result;
      }, err => {
        console.log(err);
      }
    );
  }
}
