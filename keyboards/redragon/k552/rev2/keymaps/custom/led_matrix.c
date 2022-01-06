#include <string.h>
#include "rgb.h"
#include "rgb_matrix.h"
#include "rgb_matrix_types.h"
#include "color.h"
#include "ws2812.c"
#include "config_led.h"
#include "../../../../../drivers/sn32/rgb_matrix_sn32f248b.c"

/*
    COLS key / led
    PWM PWM00A - PWM21A (PWM15A unused)
    2ty transistors PNP driven high
    base      - GPIO
    collector - LED Col pins
    emitter   - VDD

    VDD     GPIO
    (E)     (B)
     |  PNP  |
     |_______|
         |
         |
        (C)
        LED

    ROWS RGB
    PWM PWM22A - PWM21B (PWM10B unused)
    C 0-15
    j3y transistors NPN driven low
    base      - GPIO
    collector - LED RGB row pins
    emitter   - GND

        LED
        (C)
         |
         |
      _______
     |  NPN  |
     |       |
    (B)     (E)
    GPIO    GND
*/

LED_TYPE rgb_matrix_ws2812_array[RGBLED_NUM];

static void flush(void) {
    ws2812_setleds(rgb_matrix_ws2812_array, RGBLED_NUM);
}

void set_color(int index, uint8_t r, uint8_t g, uint8_t b) {
    if (index < DRIVER_LED_TOTAL - RGBLED_NUM) {
        SN32F24XX_set_color(index, r, g, b);
    } else {
        r /= 10;
        g /= 10;
        b /= 10;
        rgb_matrix_ws2812_array[index + RGBLED_NUM - DRIVER_LED_TOTAL].r = r;
        rgb_matrix_ws2812_array[index + RGBLED_NUM - DRIVER_LED_TOTAL].g = g;
        rgb_matrix_ws2812_array[index + RGBLED_NUM - DRIVER_LED_TOTAL].b = b;
        // convert_rgb_to_rgbw(&rgb_matrix_ws2812_array[index + RGBLED_NUM - DRIVER_LED_TOTAL]);
    }
}

static void set_color_all(uint8_t r, uint8_t g, uint8_t b) {
    for (int i=0; i<(DRIVER_LED_TOTAL); i++)
        set_color(i, r, g, b);
}

const rgb_matrix_driver_t rgb_matrix_driver = {
    .init          = SN32F24XX_init,
    .flush         = flush,
    .set_color     = set_color,
    .set_color_all = set_color_all,
};
