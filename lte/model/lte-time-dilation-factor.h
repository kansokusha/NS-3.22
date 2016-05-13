#ifndef LTE_TIME_DILATION_FACTOR_H
#define LTE_TIME_DILATION_FACTOR_H

#include <ns3/object.h>
#include <stdint.h>

namespace ns3 {

class LteTimeDilationFactor
{
public:
  static LteTimeDilationFactor * Get (void);

  LteTimeDilationFactor (void);
  ~LteTimeDilationFactor (void);

  void SetTimeDilationFactor (uint16_t tdf);
  uint16_t GetTimeDilationFactor (void);

private:
  static LteTimeDilationFactor * m_instance;

  uint16_t m_timeDilationFactor;
};

}

#endif
