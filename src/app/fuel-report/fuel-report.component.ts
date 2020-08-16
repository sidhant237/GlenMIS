import { Component, OnInit, OnDestroy } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import {BreakpointObserver, Breakpoints} from '@angular/cdk/layout';
import { Subscription } from 'rxjs';

import { environment } from './../../environments/environment';

export interface FuelReport {
  Machine: string;
  FuelUsed: number;
  TM: number;
  TMFuel: number;
}

@Component({
  selector: 'app-fuel-report',
  templateUrl: './fuel-report.component.html',
  styleUrls: ['./fuel-report.component.css']
})
export class FuelReportComponent implements OnInit, OnDestroy {
  displayedColumns: string[] = ['Machine', 'FuelUsed', 'TM', 'TMFuel'];
  dataSource: FuelReport[];
  startdate: any;
  enddate: any;
  startdateCmp: any;
  enddateCmp: any;
  dataSourceCmp: FuelReport[];

  mediumDevice = false;

  mediaSubscription: Subscription;

  constructor(private http: HttpClient, private breakPointObserver: BreakpointObserver) { }

  ngOnInit() {
    this.startdate = new Date();
    this.enddate = new Date();
    this.startdate.setDate(this.startdate.getDate() - 1);
    this.startdateCmp = this.startdate;
    this.enddateCmp = this.enddate;

    const url = environment.url + 'fuelreport?start=' + this.convert(this.startdate) + '&end=' + this.convert(this.enddate);
    this.http.get(url).subscribe((data: FuelReport[]) => {
      this.dataSource = data;
    });
    this.mediaChangeHandler();
  }

  ngOnDestroy() {
    this.mediaSubscription.unsubscribe();
  }

  mediaChangeHandler() {
    this.mediaSubscription = this.breakPointObserver.observe([
      '(max-width: 768px)'
        ]).subscribe(result => {
          if (result.matches === true) {
            this.mediumDevice = true;
          } else {
            this.mediumDevice = false;
          }
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

  clickedGo() {
    const url = environment.url + 'fuelreport?start=' + this.convert(this.startdate) + '&end=' + this.convert(this.enddate);
    this.http.get(url).subscribe((data: FuelReport[]) => {
      this.dataSource = data;
    });
  }

  clickedGoCompare() {
    const url = environment.url + 'fuelreport?start=' + this.convert(this.startdateCmp) + '&end=' + this.convert(this.enddateCmp);
    this.http.get(url).subscribe((data: FuelReport[]) => {
      this.dataSourceCmp = data;
    });
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
