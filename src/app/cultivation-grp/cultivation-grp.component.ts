import { Component, OnInit, OnDestroy } from '@angular/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import { HttpClient } from '@angular/common/http';
import {BreakpointObserver, Breakpoints} from '@angular/cdk/layout';
import { Subscription } from 'rxjs';

import { environment } from './../../environments/environment';


@Component({
  selector: 'app-cultivation-grp',
  templateUrl: './cultivation-grp.component.html',
  styleUrls: ['./cultivation-grp.component.css']
})
export class CultivationGrpComponent implements OnInit, OnDestroy {
  startdate: any;
  enddate: any;
  startdateCmp: any;
  enddateCmp: any;
  displayedColumns: any;
  dataSource: any;
  dataSourceCmp: any;
  stackGrid = false;

  mediaSubscription: Subscription;

  constructor(private http: HttpClient, private breakPointObserver: BreakpointObserver) {
  }

  ngOnInit() {
	this.startdate = new Date();
	this.enddate = new Date();
	this.startdate.setDate(this.startdate.getDate() - 1);
	this.startdateCmp = this.startdate;
	this.enddateCmp = this.enddate;
	this.displayedColumns = ['Job_Name', 'Mandays', 'AreaCovered', 'MndArea'];

	const url = environment.url + 'cultgroup?start=' + this.convert(this.startdate) + '&end=' + this.convert(this.enddate);
	this.http.get(url).subscribe((data: CultivationGroupByJob) => {
		this.dataSource = data;
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
		const url = environment.url + 'cultgroup?start=' + this.convert(this.startdate) + '&end=' + this.convert(this.enddate);
		this.http.get(url).subscribe((data: CultivationGroupByJob) => {
		this.dataSource = data;
		});
	}

	clickedGoCompare() {
		const url = environment.url + 'cultgroup?start=' + this.convert(this.startdateCmp) + '&end=' + this.convert(this.enddateCmp);
		this.http.get(url).subscribe((data: CultivationGroupByJob) => {
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

export interface CultivationGroupByJob {
	Job_Name: string;
	Mandays: number;
	AreaCovered: number;
	MndArea: number;
}
