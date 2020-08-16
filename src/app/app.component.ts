import { Component, OnInit, OnDestroy } from '@angular/core';
import {BreakpointObserver, Breakpoints} from '@angular/cdk/layout';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {

  title = 'glen-mis-ui-angular';
  hideSideDrawer = false;

  mediaSubscription: Subscription;

  constructor(private breakPointObserver: BreakpointObserver) {}

  ngOnInit() {
    this.mediaSubscription = this.breakPointObserver.observe([
      '(max-width: 850px)'
        ]).subscribe(result => {
          if (result.matches === true) {
            this.hideSideDrawer = true;
          } else {
            this.hideSideDrawer = false;
          }
    });
  }

  ngOnDestroy() {
    this.mediaSubscription.unsubscribe();
  }
}
