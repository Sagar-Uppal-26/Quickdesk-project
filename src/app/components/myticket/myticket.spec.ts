import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Myticket } from './myticket';

describe('Myticket', () => {
  let component: Myticket;
  let fixture: ComponentFixture<Myticket>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Myticket]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Myticket);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
