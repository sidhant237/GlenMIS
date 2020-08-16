import { Component, OnInit } from '@angular/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import { HttpClient } from '@angular/common/http';

import { environment } from './../../environments/environment';

@Component({
  selector: 'app-fine-leaf',
  templateUrl: './fine-leaf.component.html',
  styleUrls: ['./fine-leaf.component.css']
})
export class FineLeafComponent implements OnInit {
  startdate: any;
  enddate: any;
  startdateCmp: any;
  enddateCmp: any;
  displayedColumns: string[];
  dataSource: any;
  dataSourceCmp: any;

  constructor(private http: HttpClient) {
  }

  ngOnInit() {
    this.startdate = new Date();
    this.enddate = new Date();
    this.startdate.setDate(this.startdate.getDate() - 1);
    this.startdateCmp = this.startdate;
    this.enddateCmp = this.enddate;
    this.displayedColumns = ['Division', 'GLToday', 'GLTodayLY', 'FineLeaf'];

    const url = environment.url + 'GL?start=' + this.convert(this.startdate) + '&end=' + this.convert(this.enddate);
    this.http.get(url).subscribe((data: GreenLeaf) => {
      this.dataSource = data;
    });
  }

  clickedGo() {
    const url = environment.url + 'GL?start=' + this.convert(this.startdate) + '&end=' + this.convert(this.enddate);
    this.http.get(url).subscribe((data: GreenLeaf) => {
      this.dataSource = data;
    });
  }

  clickedGoCompare() {
    const url = environment.url + 'GL?start=' + this.convert(this.startdateCmp) + '&end=' + this.convert(this.enddateCmp);
    this.http.get(url).subscribe((data: GreenLeaf) => {
      this.dataSourceCmp = data;
    });
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

  getTotal(_dataSrc: string, _field: string) {
    if (this[_dataSrc]) {
      return this[_dataSrc].map(t => t[_field]).reduce((acc, value) => acc + value, 0);
    } else {
      return null;
    }
  }
  
}

export interface GreenLeaf {
  Division: string;
  GLToday: number;
  GLTodayLY: number;
  FineLeaf: number;
}
