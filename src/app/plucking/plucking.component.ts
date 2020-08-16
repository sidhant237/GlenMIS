import { Component, OnInit } from '@angular/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import { HttpClient } from '@angular/common/http';

import { environment } from './../../environments/environment';

@Component({
  selector: 'app-plucking',
  templateUrl: './plucking.component.html',
  styleUrls: ['./plucking.component.css']
})
export class PluckingComponent implements OnInit {
  startdate: any;
  enddate: any;
  startdateCmp: any;
  enddateCmp: any;
  displayedColumns: string[];
  dataSource: any;
  dataSourceCmp: any;
  showCompare: boolean;

  constructor(private http: HttpClient) {
  }

  ngOnInit() {
    this.startdate = new Date();
    this.enddate = new Date();
    this.startdate.setDate(this.startdate.getDate() - 1);
    this.startdateCmp = this.startdate;
    this.enddateCmp = this.enddate;
    this.showCompare = false;
    this.displayedColumns = [ 'Date', 'Division', 'Section_Name', 'Squad_Name', 'Mandays', 'Greenleaf',
                              'AreaCovered', 'GlMnd', 'GlHa', 'MndHa', 'Prune', 'Jat', 'SecArea'];

    const url = environment.url + 'pluckdaily?start=' + this.convert(this.startdate) + '&end=' + this.convert(this.enddate);
    this.http.get(url).subscribe((data: Plucking) => {
      this.dataSource = data;
    });
  }

  clickedGo() {
    const url = environment.url + 'pluckdaily?start=' + this.convert(this.startdate) + '&end=' + this.convert(this.enddate);
    this.http.get(url).subscribe((data: Plucking) => {
      this.dataSource = data;
    });
  }

  clickedCompare() {
    this.showCompare = true;
  }

  clickedGoCompare() {
    const url = environment.url + 'pluckdaily?start=' + this.convert(this.startdateCmp) + '&end=' + this.convert(this.enddateCmp);
    this.http.get(url).subscribe((data: Plucking) => {
      this.dataSourceCmp = data;
    });
  }

  getTotal(_dataSrc: string, _field: string) {
    if (this[_dataSrc]) {
      return this[_dataSrc].map(t => t[_field]).reduce((acc, value) => acc + value, 0);
    } else {
      return null;
    }
  }

  dateChange(type: string, event: MatDatepickerInputEvent<Date>) {
    switch (type) {
      case 'startdate': this.startdate = event.value; break;
      case 'enddate': this.enddate = event.value; break;
      case 'startdateCmp': this.startdateCmp = event.value; break;
      case 'enddateCmp': this.enddateCmp = event.value; break;
    }
  }

  convert(str) {
    var date = new Date(str),
    mnth = ("0" + (date.getMonth() + 1)).slice(-2),
    day = ("0" + date.getDate()).slice(-2);
    return [date.getFullYear(), mnth, day].join("-").toString();
  }
}

export interface Plucking {
  Date: string;
  Section_Name: string;
  Squad_Name: string;
  Mandays: number;
  Greenleaf: number;
  AreaCovered: number;
  GlMnd: number;
  GlHa: number;
  MndHa: number;
  Division: string;
  Prune: string;
  Jat: string;
  SecArea: number;
}
