import { Component, OnInit, OnDestroy } from '@angular/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import { HttpClient } from '@angular/common/http';
import {BreakpointObserver, Breakpoints} from '@angular/cdk/layout';
import { Subscription } from 'rxjs';

import { environment } from './../../environments/environment';

@Component({
  selector: 'app-daily-report',
  templateUrl: './daily-report.component.html',
  styleUrls: ['./daily-report.component.css']
})
export class DailyReportComponent implements OnInit, OnDestroy {
  startdate: any;
  teaMadeColumns: string[];
  greenLeafColumns: string[];
  GradePerColumns: string[];
  MandaysColumns: string[];
  PluckingColumns: string[];
  CultivationColumns: string[];
  FuelReportColumns: string[];

  teaMadeData: any;
  greenleafData: any;
  gradePerData: any;
  MandaysData: any;
  PluckingData: any;
  CultivationData: any;
  FuelReportData: any;
  stackGrid = false;

  mediaSubscription: Subscription;

  constructor(private http: HttpClient, private breakPointObserver: BreakpointObserver) {
  }

  ngOnInit() {
    this.startdate = new Date();
    this.startdate.setDate(this.startdate.getDate() - 1);
    this.teaMadeColumns = ['TMToday', 'TMTodate', 'TMTodateLY', 'RecoveryToday', 'RecoveryTodate'];
    this.greenLeafColumns = ['Division', 'GLToday', 'GLTodayLY', 'FineLeaf'];
    this.GradePerColumns = ['Grade', 'PercentToday', 'PercentTodate'];
    this.MandaysColumns = ['Job_Name', 'Mandays'];
    this.PluckingColumns = ['Date', 'Division', 'Section_Name', 'Squad_Name', 'Mandays', 'Greenleaf', 'AreaCovered',
                            'GlMnd', 'GlHa', 'MndHa', 'Prune', 'Jat', 'SecArea'];
    this.CultivationColumns = ['Date', 'Division', 'AreaCovered', 'Job_Name', 'Mandays', 'Mnd/Area', 'Section_Name', 'Squad_Name'];
    this.FuelReportColumns = ['Machine', 'FuelUsed', 'TM', 'TMFuel'];

    const url = environment.url + 'dailyreport?start=' + this.convert(this.startdate);
    this.http.get(url).subscribe((data: DailyReport) => {
      this.teaMadeData = data.TeaMade;
      this.greenleafData = data.Greenleaf;
      this.gradePerData = data.GradePer;
      this.MandaysData = data.Mandays;
      this.PluckingData = data.Plucking;
      this.CultivationData = data.Cultivation;
      this.FuelReportData = data.FuelReport;
    });

    this.mediaWidthHandler();
  }

  ngOnDestroy() {
    this.mediaSubscription.unsubscribe();
  }

  mediaWidthHandler() {
    this.mediaSubscription = this.breakPointObserver.observe([
      '(max-width: 700px)'
        ]).subscribe(result => {
          if (result.matches === true) {
            this.stackGrid = true;
          } else {
            this.stackGrid = false;
          }
    });
  }

  clickedGo() {
    const url = environment.url + 'dailyreport?start=' + this.convert(this.startdate);
    this.http.get(url).subscribe((data: DailyReport) => {
      this.teaMadeData = data.TeaMade;
      this.greenleafData = data.Greenleaf;
      this.gradePerData = data.GradePer;
      this.MandaysData = data.Mandays;
      this.PluckingData = data.Plucking;
      this.CultivationData = data.Cultivation;
      this.FuelReportData = data.FuelReport;
    });
  }

  dateChange(type: string, event: MatDatepickerInputEvent<Date>) {
      this.startdate = event.value;
  }

  getTotal(_dataSrc: string, _field: string) {
    if (this[_dataSrc]) {
      return this[_dataSrc].map(t => t[_field]).reduce((acc, value) => acc + value, 0);
    } else {
      return null;
    }
  }

  convert(str) {
    var date = new Date(str),
    mnth = ("0" + (date.getMonth() + 1)).slice(-2),
    day = ("0" + date.getDate()).slice(-2);
    return [date.getFullYear(), mnth, day].join("-").toString();
  }
}

export interface DailyReport {
  Greenleaf: any;
  TeaMade: any;
  Mandays: any;
  Plucking: any;
  Cultivation: any;
  GradePer: any;
  FuelReport: any;
}
