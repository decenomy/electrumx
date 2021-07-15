#ifndef X11KVS_GATE_H__
#define X11KVS_GATE_H__ 1

#include <stdint.h>

void x11kvs_hash(void *state, const void *input, uint8_t* cache);
void init_x11kv_ctx();

#endif
