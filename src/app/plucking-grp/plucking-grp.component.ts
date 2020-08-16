import { Component, OnInit } from '@angular/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import { HttpClient } from '@angular/common/http';

import { environment } from './../../environments/environment';

@Component({
  selector: 'app-plucking-grp',
  templateUrl: './plucking-grp.component.html',
  styleUrls: ['./plucking-grp.component.css']
})
export class PluckingGrpComponent implements OnInit {

  startdate: any;
  enddate: any;
  startdateCmp: any;
  enddateCmp: any;
  displayedColumns: any;
  displayedColumnsCmp: any;
  dataSource: any;
  dataSourceCmp: any;
  showCompare: boolean;
  selected: string;
  selectedCmp: string;
  group: string;
  groupCmp: string;

  constructor(private http: HttpClient) {
  }

  ngOnInit() {
    this.startdate = new Date();
    this.enddate = new Date();
    this.startdate.setDate(this.startdate.getDate() - 1);
    this.startdateCmp = this.startdate;
    this.enddateCmp = this.enddate;
    this.showCompare = false;
    this.displayedColumns = ['Division', 'Mandays', 'Greenleaf', 'AreaCovered', 'GLMnd', 'GLArea', 'MndArea'];
    this.displayedColumnsCmp = ['Division', 'Mandays', 'Greenleaf', 'AreaCovered', 'GLMnd', 'GLArea', 'MndArea'];
    this.selected = 'Division';
    this.selectedCmp = 'Division';
    this.group = 'Division';
    this.groupCmp = 'Division';

    const url = environment.url + 'pluckgroup?start=' + this.convert(this.startdate) + '&end=' + this.convert(this.enddate) + '&grpby=' + this.selected;
    this.http.get(url).subscribe((data: PluckingGroupBySection) => {
      this.dataSource = data;
    });
  }

  clickedGo() {
    const url = environment.url + 'pluckgroup?start=' + this.convert(this.startdate) + '&end=' + this.convert(this.enddate) + '&grpby=' + this.selected;
    this.http.get(url).subscribe((data: any) => {
      this.group = this.selected;
      if (this.selected === 'Section') {
        this.displayedColumns = ['Section_Name', 'Mandays', 'Greenleaf', 'AreaCovered', 'GLMnd', 'GLArea', 'MndArea'];
        this.parseSectionData('report', data);
      } else if (this.selected === 'Division') {
        this.displayedColumns = ['Division', 'Mandays', 'Greenleaf', 'AreaCovered', 'GLMnd', 'GLArea', 'MndArea'];
        this.parseDivisionData('report', data);
      } else {
        this.displayedColumns = ['Squad', 'Mandays', 'Greenleaf', 'AreaCovered', 'GLMnd', 'GLArea', 'MndArea'];
        this.parseSquadData('report', data);
      }
    });
  }

  clickedGoCompare() {
    const url = environment.url + 'pluckgroup?start=' + this.convert(this.startdateCmp) + '&end=' + this.convert(this.enddateCmp) + '&grpby=' + this.selectedCmp;
    this.http.get(url).subscribe((data: any) => {
      this.groupCmp = this.selectedCmp;
      if (this.selectedCmp === 'Section') {
        this.displayedColumnsCmp = ['Section_Name', 'Mandays', 'Greenleaf', 'AreaCovered', 'GLMnd', 'GLArea', 'MndArea'];
        this.parseSectionData('compare', data);
      } else if (this.selectedCmp === 'Division') {
        this.displayedColumnsCmp = ['Division', 'Mandays', 'Greenleaf', 'AreaCovered', 'GLMnd', 'GLArea', 'MndArea'];
        this.parseDivisionData('compare', data);
      } else {
        this.displayedColumnsCmp = ['Squad', 'Mandays', 'Greenleaf', 'AreaCovered', 'GLMnd', 'GLArea', 'MndArea'];
        this.parseSquadData('compare', data);
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
  
  parseDivisionData(type: string, data: PluckingGroupByDivision) {
    switch (type) {
      case 'report': this.dataSource = data; break;
      case 'compare': this.dataSourceCmp = data; break;
    }
  }

  parseSectionData(type: string, data: PluckingGroupBySection) {
    switch (type) {
      case 'report': this.dataSource = data; break;
      case 'compare': this.dataSourceCmp = data; break;
    }
  }

  parseSquadData(type: string, data: PluckingGroupBySquad) {
    switch (type) {
      case 'report': this.dataSource = data; break;
      case 'compare': this.dataSourceCmp = data; break;
    }
  }

}

export interface PluckingGroupBySection {
  Section_Name: string;
  Mandays: number;
  Greenleaf: number;
  AreaCovered: number;
  GLMnd: number;
  GLArea: number;
  MndArea: number;
}

export interface PluckingGroupByDivision {
  Division: string;
  Mandays: number;
  Greenleaf: number;
  AreaCovered: number;
  GLMnd: number;
  GLArea: number;
  MndArea: number;
}

export interface PluckingGroupBySquad {
  Squad: string;
  Mandays: number;
  Greenleaf: number;
  AreaCovered: number;
  GLMnd: number;
  GLArea: number;
  MndArea: number;
}
