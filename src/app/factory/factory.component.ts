import { Component, OnInit, OnDestroy } from '@angular/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import { HttpClient } from '@angular/common/http';
import {BreakpointObserver, Breakpoints} from '@angular/cdk/layout';
import { Subscription } from 'rxjs';

import { environment } from './../../environments/environment';

@Component({
  selector: 'app-factory',
  templateUrl: './factory.component.html',
  styleUrls: ['./factory.component.css']
})
export class FactoryComponent implements OnInit, OnDestroy {

  date: any;
  teaMadeColumns: string[];
  greenLeafColumns: string[];
  GradePerColumns: string[];
  teaMadeData: any;
  greenleafData: any;
  gradePerData: any;
  stackGrid = false;

  mediaSubscription: Subscription;

  constructor(private http: HttpClient, private breakPointObserver: BreakpointObserver) {
  }

  ngOnInit() {
    this.date = new Date();
    this.date.setDate(this.date.getDate() - 1);
    this.teaMadeColumns = ['TMToday', 'TMTodate', 'TMTodateLY', 'RecoveryToday', 'RecoveryTodate'];
    this.greenLeafColumns = ['Division', 'GLToday', 'GLTodayLY', 'FineLeaf'];
    this.GradePerColumns = ['Grade', 'PercentToday', 'PercentTodate'];

    const url = environment.url + 'factory?start=' + this.convert(this.date);
    this.http.get(url).subscribe((data: Factory) => {
      this.teaMadeData = data.TeaMade;
      this.greenleafData = data.Greenleaf;
      this.gradePerData = data.GradePer;
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
    const url = environment.url + 'factory?start=' + this.convert(this.date);
    this.http.get(url).subscribe((data: Factory) => {
      this.teaMadeData = data.TeaMade;
      this.greenleafData = data.Greenleaf;
      this.gradePerData = data.GradePer;
    });
  }

  dateChange(type: string, event: MatDatepickerInputEvent<Date>) {
      this.date = event.value;
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

export interface Factory {
  TeaMade: any[];
  Greenleaf: any[];
  GradePer: any[];
}
