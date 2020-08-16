import { Component, OnInit } from '@angular/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import { HttpClient } from '@angular/common/http';

import { environment } from './../../environments/environment';

@Component({
	selector: 'app-cultivation',
	templateUrl: './cultivation.component.html',
	styleUrls: ['./cultivation.component.css']
})
export class CultivationComponent implements OnInit {

	startdate; enddate; startdateCmp; enddateCmp; displayedColumns; dataSource; dataSourceCmp;

	//dev purpose
	//_startdate = '2020-07-01';
	//_enddate = '2020-07-14';

	constructor(private http: HttpClient) {
	}

	ngOnInit() {
		this.startdate = new Date();
		this.enddate = new Date();
		this.startdate.setDate(this.startdate.getDate() - 1);
		this.startdateCmp = this.startdate;
		this.enddateCmp = this.enddate;
		this.displayedColumns = ['Date', 'Division', 'AreaCovered', 'Job_Name', 'Mandays', 'Mnd/Area', 'Section_Name', 'Squad_Name'];

		const url = environment.url + 'cultdaily?start=' + this.convert(this.startdate) + '&end=' + this.convert(this.enddate);
		this.http.get(url).subscribe((data: ICultivation) => {
			this.dataSource = data;
		});
	}

	clickedGo() {
		const url = environment.url + 'cultdaily?start=' + this.convert(this.startdate) + '&end=' + this.convert(this.enddate);
		this.http.get(url).subscribe((data: ICultivation) => {
			this.dataSource = data;
		});
	}

	clickedGoCompare() {
		const url = environment.url + 'cultdaily?start=' + this.convert(this.startdateCmp) + '&end=' + this.convert(this.enddateCmp);
		this.http.get(url).subscribe((data: ICultivation) => {
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

export interface ICultivation {
	Date: string;
	Job_Name: string;
	Section_Name: string;
	Squad_Name: string;
	Mandays: number;
	AreaCovered: number;
	Mnd_Area: number;
	Division: string;
}
