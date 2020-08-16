import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material-module';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

// components
import { CultivationComponent } from './cultivation/cultivation.component';
import { CultivationGrpComponent } from './cultivation-grp/cultivation-grp.component';
import { PluckingComponent } from './plucking/plucking.component';
import { PluckingGrpComponent } from './plucking-grp/plucking-grp.component';
import { MndDeploymentComponent } from './mnd-deployment/mnd-deployment.component';
import { FuelReportComponent } from './fuel-report/fuel-report.component';
import { TeaStockComponent } from './tea-stock/tea-stock.component';
import { FineLeafComponent } from './fine-leaf/fine-leaf.component';
import { InvoiceListComponent } from './invoice-list/invoice-list.component';
import { UploadFileComponent } from './upload-file/upload-file.component';
import { FactoryComponent } from './factory/factory.component';
import { SpinnerComponent } from './shared/spinner/spinner.component';
import { DailyReportComponent } from './daily-report/daily-report.component';
import { GradePerComponent } from './grade-per/grade-per.component';

@NgModule({
  declarations: [
    AppComponent,
    CultivationComponent,
    CultivationGrpComponent,
    PluckingComponent,
    PluckingGrpComponent,
    MndDeploymentComponent,
    FuelReportComponent,
    TeaStockComponent,
    FineLeafComponent,
    InvoiceListComponent,
    UploadFileComponent,
    FactoryComponent,
    SpinnerComponent,
    DailyReportComponent,
    GradePerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
