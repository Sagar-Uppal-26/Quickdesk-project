import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Submitticket } from './submitticket';

describe('Submitticket', () => {
  let component: Submitticket;
  let fixture: ComponentFixture<Submitticket>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Submitticket]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Submitticket);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
