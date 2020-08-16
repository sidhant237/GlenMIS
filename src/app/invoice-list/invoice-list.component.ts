import { Component, OnInit } from '@angular/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import { HttpClient } from '@angular/common/http';

import { environment } from './../../environments/environment';

@Component({
  selector: 'app-invoice-list',
  templateUrl: './invoice-list.component.html',
  styleUrls: ['./invoice-list.component.css']
})
export class InvoiceListComponent implements OnInit {
  startdate: any;
  enddate: any;
  displayedColumns: string[];
  dataSource: Invoice;

  constructor(private http: HttpClient) {
  }

  ngOnInit() {
    this.startdate = new Date();
    this.enddate = new Date();
    this.startdate.setDate(this.startdate.getDate() - 1);
    this.displayedColumns = ['InvNo', 'Grade', 'NetWt', 'Papersacks', 'Packdate'];

    const url = environment.url + 'invoicelist?start=' + this.convert(this.startdate) + '&end=' + this.convert(this.enddate);
    this.http.get(url).subscribe((data: Invoice) => {
    this.dataSource = data;
    });
  }

  clickedGo() {
    const url = environment.url + 'invoicelist?start=' + this.convert(this.startdate) + '&end=' + this.convert(this.enddate);
    this.http.get(url).subscribe((data: Invoice) => {
      this.dataSource = data;
    });
  }

  dateChange(type: string, event: MatDatepickerInputEvent<Date>) {
    switch (type) {
      case 'startdate': this.startdate = event.value; break;
      case 'enddate': this.enddate = event.value; break;
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

export interface Invoice {
  InvNo: string;
  Grade: string;
  NetWt: string;
  Papersacks: string;
  Packdate: number;
}
