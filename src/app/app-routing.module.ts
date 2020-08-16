import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

// componets
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
import { DailyReportComponent } from './daily-report/daily-report.component';


const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: DailyReportComponent },
  { path: 'cultdaily', component: CultivationComponent },
  { path: 'cultgroup', component: CultivationGrpComponent },
  { path: 'pluckdaily', component: PluckingComponent },
  { path: 'pluckgroup', component: PluckingGrpComponent },
  { path: 'mnddeploy', component: MndDeploymentComponent },
  { path: 'fuelreport', component: FuelReportComponent },
  { path: 'teastock', component: TeaStockComponent },
  { path: 'fineleaf', component: FineLeafComponent},
  { path: 'invoicelist', component: InvoiceListComponent},
  { path: 'upload-csv', component: UploadFileComponent},
  { path: 'factory', component: FactoryComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
