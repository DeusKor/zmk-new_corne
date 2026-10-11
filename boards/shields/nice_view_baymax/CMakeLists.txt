# Peripheral-only artwork variant; hardware and status widgets match upstream nice_view.
if(CONFIG_ZMK_DISPLAY AND CONFIG_NICE_VIEW_WIDGET_STATUS)
  if(CONFIG_ZMK_SPLIT_ROLE_CENTRAL)
    message(FATAL_ERROR "nice_view_baymax is only for the peripheral/right half")
  endif()
  zephyr_library_include_directories(${CMAKE_SOURCE_DIR}/include)
  zephyr_library_sources(custom_status_screen.c widgets/bolt.c widgets/util.c
                         widgets/baymax.c widgets/peripheral_status.c)
endif()
