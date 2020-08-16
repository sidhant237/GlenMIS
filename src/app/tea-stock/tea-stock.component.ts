import { Component, OnInit, OnDestroy } from '@angular/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import { HttpClient } from '@angular/common/http';
import {BreakpointObserver, Breakpoints} from '@angular/cdk/layout';
import { Subscription } from 'rxjs';

import { environment } from './../../environments/environment';


@Component({
  selector: 'app-tea-stock',
  templateUrl: './tea-stock.component.html',
  styleUrls: ['./tea-stock.component.css']
})
export class TeaStockComponent implements OnInit, OnDestroy {
  startdate: any;
  displayedColumns: string[];
  dataSource: TeaStock;
  meduimScreen = false;

  mediaSubscription: Subscription;

  constructor(private http: HttpClient, private breakPointObserver: BreakpointObserver) {
  }

  ngOnInit() {
    this.startdate = new Date();
    this.startdate.setDate(this.startdate.getDate() - 1);
    this.displayedColumns = ['Grade', 'Kg' ];

    const url = environment.url + 'teastock?start=' + this.convert(this.startdate);
    this.http.get(url).subscribe((data: TeaStock) => {
    this.dataSource = data;
    });

    this.mediumScreenHandler();
  }

  ngOnDestroy() {
    this.mediaSubscription.unsubscribe();
  }

  mediumScreenHandler() {
    this.mediaSubscription = this.breakPointObserver.observe([
      '(max-width: 850px)'
        ]).subscribe(result => {
          if (result.matches === true) {
            this.meduimScreen = true;
          } else {
            this.meduimScreen = false;
          }
    });
  }

  clickedGo() {
    const url = environment.url + 'teastock?start=' + this.convert(this.startdate);
    this.http.get(url).subscribe((data: TeaStock) => {
      this.dataSource = data;
    });
  }

  dateChange(type: string, event: MatDatepickerInputEvent<Date>) {
      this.startdate = event.value;
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

export interface TeaStock {
  Grade: string;
  Kg: number;
}
